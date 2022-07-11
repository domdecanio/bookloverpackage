import unittest
from booklover_bin.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        test1 = BookLover("test1", "test1@gmail.com", "test1_genre")
        test1.add_book("Test1_book", 10)
        
        # Will be "True" if operation completed successfully
        testValue = (len(test1.book_list) > 0) 
        # This message will be displayed if the operation was unsuccessful.
        message = 'The "added" book is not in the book_list.' 
        self.assertTrue(testValue, message)


    def test_2_add_book(self):
        test2 = BookLover("test2", "test2@gmail.com", "test2_genre")
        test2.add_book("Test2_book", 10)
        test2.add_book("Test2_book", 10)
        test2.add_book("Test2_book", 10)
        
        # Will be "False" if operation completed successfully
        testValue = (len(list(test2.book_list[test2.book_list['book_name'] == 'Test2_book']))) > 2 
        # This message will be displayed if the operation was unsuccessful.
        message = 'The "added" book has two entries in the "book_list".' 
        self.assertFalse(testValue, message)
            
            
    def test_3_has_read(self): 
        test3 = BookLover("test3", "test3@gmail.com", "test3_genre")
        test3.add_book("Test3_book", 10)
        
        # Will be "True" if operation completed successfully
        testValue = test3.has_read("Test3_book") 
        # This message will be displayed if the operation was unsuccessful.
        message = 'The ".has_read()" method is not capturing added books.' 
        self.assertTrue(testValue, message)
        
        
    def test_4_has_read(self): 
        test4 = BookLover("test4", "test4@gmail.com", "test4_genre")
        test4.add_book("Test4_book", 10)
        
        # Will be "False" if operation completed successfully
        testValue = test4.has_read("Test4_book2") 
        # This message will be displayed if the operation was unsuccessful.
        message = 'The ".has_read()" method incorrectly states that books not in "book_list" are contained therein.' 
        self.assertFalse(testValue, message)
        
        
    def test_5_num_books_read(self): 
        test5 = BookLover("test5", "test5@gmail.com", "test5_genre")
        test5.add_book("Test5_book1", 10)
        test5.add_book("Test5_bookj", 2)
        test5.add_book("Test5_book3k", 4)
        test5.add_book("Test5_book99", 7)
        
        # Will be "True" if operation completed successfully
        testValue = test5.num_books_read() == 4 
        # This message will be displayed if the operation was unsuccessful.
        message = 'The ".num_books_read()" method does not correctly indicate the number of books stored in the "book_list" object.' 
        self.assertTrue(testValue, message)
        
        
    def test_6_fav_books(self):
        test6 = BookLover("test6", "test6@gmail.com", "test6_genre")
        test6.add_book("Test6_booka", 4)
        test6.add_book("Test6_bookbravado", 1)
        test6.add_book("Test6_bookc", 0)
        test6.add_book("Test6_bookdeltoid", 9)\
        
        # Will be "True" if operation completed successfully
        testValue = list(test6.fav_books()['book_name']) == ['Test6_booka', 'Test6_bookdeltoid'] 
        # This message will be displayed if the operation was unsuccessful.
        message = 'The ".fav_books()" method does not correctly identify books with a rating > 3.' 
        self.assertTrue(testValue, message)
                
            
if __name__ == '__main__':
    unittest.main(verbosity=3)