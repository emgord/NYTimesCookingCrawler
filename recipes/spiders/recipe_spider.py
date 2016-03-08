import scrapy

from recipes.items import RecipeItem, IngredientItem

class RecipeSpider(scrapy.Spider):
    name = "recipe"
    allowed_domains = ["http://cooking.nytimes.com/"]
    start_urls = [
        "http://cooking.nytimes.com/recipes/12790"
    ]

    def parse(self, response):
        recipe = RecipeItem()
        recipe['title'] = response.xpath('/html/body/div[2]/div/div[1]/article/header/h1/text()').extract()[0].strip()
        recipe['image'] = response.xpath('/html/body/div[2]/div/div[1]/article/div[1]/div[1]/img/@src').extract()[0]
        recipe['recipe_yield'] = response.xpath('/html/body/div[2]/div/div[1]/article/header/div[1]/ul/li[2]/span[2]/text()').extract()[0].strip()
        recipe['time'] = response.xpath('/html/body/div[2]/div/div[1]/article/header/div[1]/ul/li[1]/text()').extract()[2].strip()
        recipe['original_url'] = response.xpath('/html/body/div[2]/div/div[1]/article/@data-url').extract()[0]
        recipe['description'] = response.xpath('/html/body/div[2]/div/div[1]/article/div[1]/div[2]/div/p[1]/text()').extract()[0].strip()
        recipe['uid'] = response.xpath('/html/body/div[2]/div/div[1]/article/@data-id').extract()[0]
        recipe['ingredients'] = []
        for ingredient in response.xpath('//li[@itemprop="recipeIngredient"]'):
            # name = ingredient.xpath('span[@class="ingredient-name"]/span/text()').extract()[0]
            recipe['ingredients'].append("hello")
        yield recipe

        # for ingredient in response.xpath('//li[@itemprop="recipeIngredient"]'):
        #     item = IngredientItem()
        #     item['name'] = ingredient.xpath('span[@class="ingredient-name"]/span/text()').extract()[0]
        #     item['recipe_id'] = response.xpath('/html/body/div[2]/div/div[1]/article/@data-id').extract()[0]
        #     ingredients.append(item)
        #



# title: response.xpath('/html/body/div[2]/div/div[1]/article/header/h1/text()').extract()[0].strip()

# time : response.xpath('/html/body/div[2]/div/div[1]/article/header/div[1]/ul/li[1]/text()').extract()[2].strip()

# yield : response.xpath('/html/body/div[2]/div/div[1]/article/header/div[1]/ul/li[2]/span[2]/text()').extract()[0].strip()

# description: response.xpath('/html/body/div[2]/div/div[1]/article/div[1]/div[2]/div/p[1]/text()').extract()[0].strip()

# image: response.xpath('/html/body/div[2]/div/div[1]/article/div[1]/div[1]/img/@src').extract()[0]

# id: response.xpath('/html/body/div[2]/div/div[1]/article/@data-id').extract()
#
# url: response.xpath('/html/body/div[2]/div/div[1]/article/@data-url').extract()

# ingredients:
#
# response.xpath(' /html/body/div[2]/div/div[1]/article/div[3]/section[1]/ul[1]/li" need to iterate through li and do this to each one for each ingredient:
#
# [5]/span[2]/span/text()').extract()

# response.xpath(' /html/body/div[2]/div/div[1]/article/div[3]/section[1]/ul[1]/li')[1].xpath("span[2]/span/text()").extract()
#
# ingredients = response.xpath('/html/body/div[2]/div/div[1]/article/div[3]/section[1]/ul[1]/li')
# for ingredient in ingredients:
#     ings = []
#     i = ingredient.xpath("span[2]/span/text()").extract()
#     ings.append(i)
#     yield ings
