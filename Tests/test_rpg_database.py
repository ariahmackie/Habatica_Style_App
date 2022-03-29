import unittest
import rpg_database as rpg

class TestPlayerTable(unittest.TestCase):
    def setUp(self):
        rpg.drop_all_tables()


    def tearDown(self):
        pass


    def set_up_player(self):
        rpg.create_player_table()
        rpg.add_new_player("adm@gmail.com", "Adam", "1234")

    def set_up_inventory(self):
        self.set_up_player()
        rpg.create_stock_table()
        rpg.populate_stock_table()
        rpg.create_inventory_table()

    def set_up_tasks(self):
        self.set_up_player()
        rpg.create_task_table()

    def drop_tables(self):
        rpg.drop_all_tables()

    def test_add_new_player(self):
        rpg.create_player_table()
        rpg.add_new_player("adm@gmail.com", "Adam", "1234")
        expected_tuple = (1, 'adm@gmail.com', 'Adam', '1234', 1, 1, 100, 0, 100, 0, 0, 0, 0, None)
        actual_tuple = rpg.get_player(1)
        self.assertEqual(expected_tuple, actual_tuple, "tuples should be the same")
        self.drop_tables()

    def test_find_players_with_feature(self):
        self.set_up_player()
        actual_person = rpg.find_players_with_feature("username", "Ashley")  # search a name that isn't in the database
        expected_person = None
        self.assertEqual(actual_person, expected_person, "should return nothing because 'Ashley' is not in the database")
        

    def test_get_value_from_player(self):
        self.set_up_player()
        actual_email = rpg.get_value_from_player("email", 1)
        expected_email = "adm@gmail.com"
        self.assertEqual(expected_email, actual_email, "emails should be the same")
        self.drop_tables()

    def test_change_value_in_player(self):
        self.set_up_player()
        rpg.change_value_in_player("username", "Mary", 1)
        actual_username = rpg.get_value_from_player("username", 1)
        expected_username = "Mary"
        self.assertEqual(actual_username, expected_username, "Names should be the same")
        self.drop_tables()

    def test_decrease_value_in_player(self):
        self.set_up_player()
        rpg.decrease_value_from_player("health", 2, 1)
        expected_health = 98
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should have decreased by 2")
        self.drop_tables()

    def test_increase_value_in_player(self):
        self.set_up_player()
        rpg.increase_value_in_player("strength", 2, 1)
        expected_strength = 2
        actual_strength = rpg.get_value_from_player("strength", 1)
        self.assertEqual(expected_strength, actual_strength, "strength should be raised by 2")
        self.drop_tables()

    def test_increase_health_in_player(self):
        self.set_up_player()
        rpg.increase_health(1, 5)
        expected_health = 100
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should only be 100 because it can't go past 1100")
        self.drop_tables()

    def test_decrease_health_in_player(self):
        self.set_up_player()
        rpg.decrease_health(1, 50)
        expected_health = 50
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should decrease by 50")
        rpg.decrease_health(1, 55)
        expected_health = 0
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should be 0 and not negative")
        self.drop_tables()

    def test_add_item_by_id(self):
        self.set_up_inventory()
        rpg.add_item_by_id(2, 1)
        actual_item = rpg.get_item_by_id(1)
        expected_item = (1, "banana", 1,  2, 1)
        self.assertEqual(actual_item, expected_item, "should return banana item")
        self.drop_tables()

    def test_add_item_by_name(self):
        self.set_up_inventory()
        rpg.add_item_by_name("berries", 1)
        actual_item = rpg.get_item_by_id(1)
        expected_item = (1, "berries", 1, 3, 1)
        self.assertEqual(actual_item, expected_item, "item should be berries")
        self.drop_tables()

    def test_add_item(self):
        self.set_up_inventory()
        item_tuple = (1, "cheese", 2, "meal")
        rpg.add_item(item_tuple, 1)
        actual_item = rpg.get_item_by_id(1)
        expected_item = (1, "cheese", 1, 1, 1)
        self.assertEqual(actual_item, expected_item, "item should be cheese")
        self.drop_tables()

    def test_count_how_many_of_item(self):
        self.set_up_inventory()
        rpg.add_item_by_id(1, 1)
        actual_count = rpg.count_how_many_of_item("apple", 1)
        expected_count = 1
        self.assertEqual(actual_count, expected_count, "count should be 1")
        self.drop_tables()

    def test_select_stockitem_by_id(self):
        self.set_up_inventory()
        actual_item = rpg.select_stockitem_by_id(1)
        expected_item = (1, "apple", 2, "fruit", None)
        self.assertEqual(actual_item, expected_item, "Should return apple tuple")
        self.drop_tables()

    def test_select_stockitem_by_name(self):
        self.set_up_inventory()
        actual_item = rpg.select_stockitem_by_name("apple")
        expected_item = (1, "apple", 2, "fruit", None)
        self.assertEqual(actual_item, expected_item, "should return apple tuple")
        self.drop_tables()

    def test_get_num_items_in_stock(self):
        self.set_up_inventory()
        expected_number = 57
        actual_number = rpg.get_num_items_in_stock()
        self.assertEqual(actual_number, expected_number, "should return 57")
        self.drop_tables()

    def test_create_task_and_get_task(self):
        self.set_up_tasks()
        rpg.create_task("work on homework", "3-12-21", 4,  0, 1)
        actual_task = rpg.get_task_by_id(1)
        expected_task = (1, "work on homework", "3-12-21", 4, 0, 1, 0)
        self.assertEqual(actual_task, expected_task, "should return same task")
        self.drop_tables()

    def test_return_all_task_by_player(self):
        self.set_up_tasks()
        rpg.create_task("person 1 task 1", "date", 4, 0, 1)
        rpg.create_task("person 1 task 2", "date", 4, 0, 1)
        rpg.create_task("person 1 task 3", "date", 4, 0, 1)
        rpg.create_task("person 2 task 1", "date", 4, 0, 2)
        rpg.create_task("person 2 task 2", "date", 4, 0, 2)
        tasks = rpg.return_player_tasks(1)
        actual_tasklist = []
        #(id, description, duedate, value, isreeapable, playerid, complete)
        expected_tasklist = [(1, "person 1 task 1", "date", 4, 0, 1, 0), (2, "person 1 task 2", "date", 4, 0, 1, 0), (3,"person 1 task 3", "date", 4, 0, 1, 0)]
        for i in tasks:
            actual_tasklist.append(i)
        self.assertEqual(actual_tasklist, expected_tasklist, "should be a list of only tasks from player 1")
        self.drop_tables()

    def test_change_value_in_task(self):
        self.set_up_tasks()
        rpg.create_task("person 1 task 1", "date", 4, 0, 1)
        rpg.change_value_in_task("description", "mow lawn", 1)
        actual_task = rpg.get_task_by_id(1)
        expected_task = (1, "mow lawn", "date", 4, 0, 1, 0)
        self.assertEqual(actual_task, expected_task, "task should be the same")
        self.drop_tables()

    def test_get_task_feature_by_id(self):
        self.set_up_tasks()
        rpg.create_task("mow lawn", "date", 4, 0, 1)
        actual_date = rpg.get_task_feature_by_id("duedate", 1)
        expected_date = "date"
        self.assertEqual(actual_date, expected_date, "dates should be the same string")
        self.drop_tables()

    def test_delete_task(self):
        self.set_up_tasks()
        rpg.create_task("mow lawn", "date", 4, 0, 1)
        rpg.create_task("pay insurance", "date", 4, 0, 1)
        rpg.delete_task(1)
        leftover_task = rpg.return_player_tasks(1)[0]
        expected_task = (2, "pay insurance", "date", 4, 0, 1, 0)
        self.assertEqual(leftover_task, expected_task, "2nd tasks should be left")
        self.drop_tables()

    def test_complete_task(self):
        self.set_up_tasks()
        rpg.create_task("mow lawn", "date", 4, 0, 1)
        rpg.complete_task(1)
        actual_task = rpg.get_task_by_id(1)
        expected_task = (1, "mow lawn", "date", 4, 0, 1, 1)
        self.assertEqual(actual_task, expected_task, "last feature should be a 1 now that the test is complete")
        self.drop_tables()




if __name__ == "__main__":
    unittest.main()
