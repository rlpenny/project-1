import unittest
import proj1_w18 as proj1


class TestMedia(unittest.TestCase):

    def testMediaConstructor(self):
        #testing constructor
        m2 = proj1.Media("1999", "Prince", "1982")

        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.year, "1982")

        #testing length
        self.assertEqual(m2.__len__(), 0)

        #testing string
        self.assertEqual(m2.__str__(), "1999 by Prince (1982)")

        #is printing out 3 lines
        #print(m2.__str__())

    def testSongConstructor(self):
        #testing constructor
        s2 = proj1.Song("Halo", "Beyonce", "2008", "I am... Sasha Fierce", "Pop", "3:44")

        self.assertEqual(s2.title, "Halo")
        self.assertEqual(s2.author, "Beyonce")
        self.assertEqual(s2.year, "2008")
        self.assertEqual(s2.album, "I am... Sasha Fierce")
        self.assertEqual(s2.genre, "Pop")
        self.assertEqual(s2.length, "3:44")

        #testing length

        self.assertEqual(s2.__len__(), s2.length)

        #testing string
        self.assertEqual(s2.__str__(), "Halo by Beyonce (2008)[Pop]")

    def testMovieConstructor(self):

        #testing constructor
        mo2= proj1.Movies("Finding Nemo", "Pixar", "2003", "G", "6000000")

        self.assertEqual(mo2.title, "Finding Nemo")
        self.assertEqual(mo2.author, "Pixar")
        self.assertEqual(mo2.year, "2003")
        self.assertEqual(mo2.rating, "G")
        self.assertEqual(mo2.movie_length, "6000000")

        #testing length
        self.assertEqual(mo2.__len__(), 100.0)

        #testing string
        self.assertEqual(mo2.__str__(), "Finding Nemo by Pixar (2003)[G]")


    def testInstanceVars(self):
        m2 = proj1.Media("1999", "Prince", "1982")
        mo2= proj1.Movies("Finding Nemo", "Pixar", "2003", "G", "6000000")
        s2 = proj1.Song("Halo", "Beyonce", "2008", "I am... Sasha Fierce", "Pop", "3:44")

        #hasattr returns false if it is not an attribute
        #checking that nonmovie classes do not have attribute rating
        if hasattr(s2, "rating") == True:
            fail()

        if hasattr(m2, "rating") == True:
            fail()

        #media and song does not have album
        if hasattr(mo2, "album") == True:
            fail()

        if hasattr(m2, "album") == True:
            fail()

        #media and movie does not have genre
        if hasattr(m2, "genre") == True:
            fail()

        if hasattr(mo2, "genre") == True:
            fail()

        #song and media does not have movie_length
        if hasattr(m2, "movie_length") == True:
            fail()

        if hasattr(s2, "movie_length") == True:
            fail()

        #movie and media does not have track_length
        if hasattr(mo2, "length") == True:
            fail()

        if hasattr(m2, "length") == True:
            fail()











unittest.main()
