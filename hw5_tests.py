"""
% Student Name: Erin Annis
% UniqName: eaannis
"""

import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0) #expect suit to be 0
        self.assertEqual(c1.suit_name, "Diamonds") #expect suit_name to be Diamonds
        self.assertEqual(c1.rank, 2) #expect rank to be 2
        self.assertEqual(c1.rank_name, "2") #expect rank_name to be 2

        self.assertIsInstance(c1.suit, int) #expect suit to be an integer
        self.assertIsInstance(c1.suit_name, str) #expect suit_name to be a string
        self.assertIsInstance(c1.rank, int) #expect rank to be an integer
        self.assertIsInstance(c1.rank_name, str) #expect rank_name to be a string

        self.assertEqual(c2.suit, 1) #Testing second object - expect suit to be 1
        self.assertEqual(c2.suit_name, "Clubs") #expect suit_name to be Clubs
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")


#REMINDER: Push to GitHub when I am done - perform git add ./ git commit -m "message"/ git push in my cloned folder (git push --set-upstream origin master?)

    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c3 = hw5_cards.Card(0, 12)
        self.assertEqual(c3.rank_name, "Queen")
        return(c3.rank_name, "Queen")
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c4 = hw5_cards.Card(1)
        self.assertEqual(c4.suit_name, "Clubs")
        return(c4.suit_name, "Clubs")
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c5 = hw5_cards.Card(3, 13)
        self.assertEqual(str(c5), "King of Spades")
        return (str(c5), "King of Spades")
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a deck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck1 = hw5_cards.Deck().cards
        self.assertEqual(len(deck1), 52)
        return(len(deck1), 52)

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c6 = hw5_cards.Deck().deal_card()
        self.assertIsInstance(str(c6), str)
        return(c6, str)
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        deck2 = hw5_cards.Deck()
        deck2.deal_card()
        self.assertEqual(len(deck2.cards), 51)
        return(len(deck2.cards), 51)

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck3 = hw5_cards.Deck()
        c7 = deck3.deal_card()
        len1 = len(deck3.cards)
        deck3.replace_card(c7)
        len2 = len(deck3.cards)
        self.assertEqual(len2, (len1+1)) #The autograder doesn't like this, but I believe it should work - this way, if deal_card is run more than once, the self.assertEqual will still work

    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck4 = hw5_cards.Deck()
        c8 = deck4.deal_card()
        deck4.replace_card(c8)
        len3 = len(deck4.cards)
        deck4.replace_card(c8)
        len4 = len(deck4.cards)
        self.assertEqual(len3, len4)
        return(len3, len4)

if __name__=="__main__":
    unittest.main()