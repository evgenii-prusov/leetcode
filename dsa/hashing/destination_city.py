from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_city: set[str] = set()
        for cities in paths:
            from_city.add(cities[0])

        for cities in paths:
            if cities[1] not in from_city:
                return cities[1]
