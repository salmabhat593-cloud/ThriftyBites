def compare_prices(cart, food_items):
    platforms = ['BigBasket', 'Blinkit', 'Amazon', 'DMart']
    platform_costs = {platform: 0 for platform in platforms}
    for item in cart:
        for platform in platforms:
            for food in food_items:
                if food['name'] == item['name']:
                    platform_costs[platform] += food['price'][platform]
    return platform_costs
