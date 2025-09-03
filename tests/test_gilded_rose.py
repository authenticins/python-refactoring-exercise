# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    
    def test_normal_item_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)
    
    def test_normal_item_on_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
    
    def test_normal_item_after_sell_date(self):
        items = [Item("Normal Item", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
    
    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_normal_item_quality_never_negative_after_sell_date(self):
        items = [Item("Normal Item", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


class AgedBrieTest(unittest.TestCase):
    
    def test_aged_brie_before_sell_date(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_aged_brie_on_sell_date(self):
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
    
    def test_aged_brie_after_sell_date(self):
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
    
    def test_aged_brie_quality_never_above_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_aged_brie_quality_never_above_50_after_sell_date(self):
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


class SulfurasTest(unittest.TestCase):
    
    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
    
    def test_sulfuras_never_changes_on_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
    
    def test_sulfuras_never_changes_after_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


class BackstagePassesTest(unittest.TestCase):
    
    def test_backstage_passes_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_backstage_passes_exactly_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
    
    def test_backstage_passes_between_6_and_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
    
    def test_backstage_passes_exactly_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)
    
    def test_backstage_passes_less_than_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(23, items[0].quality)
    
    def test_backstage_passes_on_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_backstage_passes_after_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_backstage_passes_quality_never_above_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


class EdgeCaseTest(unittest.TestCase):
    
    def test_quality_boundary_normal_item_at_50(self):
        items = [Item("Normal Item", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(49, items[0].quality)
    
    def test_quality_boundary_aged_brie_at_49(self):
        items = [Item("Aged Brie", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_multiple_items_update(self):
        items = [
            Item("Normal Item", 10, 20),
            Item("Aged Brie", 10, 20),
            Item("Sulfuras, Hand of Ragnaros", 10, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(19, items[0].quality)
        self.assertEqual(21, items[1].quality)
        self.assertEqual(80, items[2].quality)
        self.assertEqual(22, items[3].quality)


if __name__ == '__main__':
    unittest.main()
