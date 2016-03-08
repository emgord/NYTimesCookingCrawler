import scrapy

from recipes.items import RecipeItem

class RecipeSpider(scrapy.Spider):
    name = "recipe"
    allowed_domains = ["http://cooking.nytimes.com/"]
    start_urls = [
        "http://cooking.nytimes.com/recipes/100"
    ]

    def parse(self, response):
        recipe = RecipeItem()
        title = response.xpath('//h1[@itemprop="name"]/@data-name').extract()
        if len(title) > 0:
            recipe['title'] = title[0].strip()
        image = response.xpath('//img[@itemprop="image"]/@src').extract()
        if len(image) > 0:
            recipe['image'] = image[0]
        recipe_yield = response.xpath('//span[@itemprop="recipeYield"]/text()').extract()
        if len(recipe_yield) > 0:
            recipe['recipe_yield'] = recipe_yield[0].strip()
        time = response.xpath('//ul[@class="recipe-time-yield"]/li[1]/text()').extract()
        if len(time) > 2:
            recipe['time'] = time[2].strip()
        original_url = response.xpath('//article[@data-analytics-category="Recipe Detail Full"]/@data-url').extract()
        if len(original_url) > 0:
            recipe['original_url'] = original_url[0]
        uid = response.xpath('//article[@data-analytics-category="Recipe Detail Full"]/@data-id').extract()
        if len(uid) > 0:
            recipe['uid'] = uid[0]
        description = response.xpath('//div[@itemprop="description"]/p[1]/text()').extract()
        if len(description) > 0:
            recipe['description'] = description[0].strip()
        recipe['ingredients'] = []
        for ingredient in response.xpath('//li[@itemprop="recipeIngredient"]'):
            name = ingredient.xpath('span[@class="ingredient-name"]/span/text()').extract()
            if len(name) > 0:
                recipe['ingredients'].append(name[0])
        yield recipe
