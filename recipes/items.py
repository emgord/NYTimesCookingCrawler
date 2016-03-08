# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    recipe_yield = scrapy.Field()
    time = scrapy.Field()
    original_url = scrapy.Field()
    description = scrapy.Field()
    uid = scrapy.Field()

class IngredientItem(scrapy.Item):
    name = scrapy.Field()
    recipe_id = scrapy.Field()
