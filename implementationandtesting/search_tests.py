from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        metadata = [['Kevin Cadogan', 'Mr Jake', 1144136316, 3917, ['cadogan', 'record', 'and', 'the', 'band', 'third', 'eye', 'blind', 'with', 'from', 'their', 'album', 'his', 'jenkins', 'recording', 'elektra', 'records', 'was', 'for', 'california', 'two', 'music', 'that', 'have', 'were']]]
        expected_keyword_to_titles_results = {'cadogan': ['Kevin Cadogan'], 'record': ['Kevin Cadogan'], 'and': ['Kevin Cadogan'], 'the': ['Kevin Cadogan'], 'band': ['Kevin Cadogan'], 'third': ['Kevin Cadogan'], 'eye': ['Kevin Cadogan'], 'blind': ['Kevin Cadogan'], 'with': ['Kevin Cadogan'], 'from': ['Kevin Cadogan'], 'their': ['Kevin Cadogan'], 'album': ['Kevin Cadogan'], 'his': ['Kevin Cadogan'], 'jenkins': ['Kevin Cadogan'], 'recording': ['Kevin Cadogan'], 'elektra': ['Kevin Cadogan'], 'records': ['Kevin Cadogan'], 'was': ['Kevin Cadogan'], 'for': ['Kevin Cadogan'], 'california': ['Kevin Cadogan'], 'two': ['Kevin Cadogan'], 'music': ['Kevin Cadogan'], 'that': ['Kevin Cadogan'], 'have': ['Kevin Cadogan'], 'were': ['Kevin Cadogan']}
        self.assertEqual(keyword_to_titles(metadata), expected_keyword_to_titles_results)
        metadata = []        
        expected_keyword_to_titles_results = {}
        self.assertEqual(keyword_to_titles(metadata), expected_keyword_to_titles_results)
        metadata = [['1922 in music', 'Gary King', 1242717698, 11576, ['music', 'the', '1922', 'january', 'first', 'may', 'orchestra', 'radio', 'october', 'and', 'for', 'paul', 'walter', 'george', 'billy', 'harry', 'you', 'march', 'april', 'production', 'opened', 'theatre', 'september', 'ran', 'performances', 'august', 'american', 'singer', 'actress', 'composer', 'june']], ]
        expected_keyword_to_titles_results = {'music': ['1922 in music'], 'the': ['1922 in music'], '1922': ['1922 in music'], 'january': ['1922 in music'], 'first': ['1922 in music'], 'may': ['1922 in music'], 'orchestra': ['1922 in music'], 'radio': ['1922 in music'], 'october': ['1922 in music'], 'and': ['1922 in music'], 'for': ['1922 in music'], 'paul': ['1922 in music'], 'walter': ['1922 in music'], 'george': ['1922 in music'], 'billy': ['1922 in music'], 'harry': ['1922 in music'], 'you': ['1922 in music'], 'march': ['1922 in music'], 'april': ['1922 in music'], 'production': ['1922 in music'], 'opened': ['1922 in music'], 'theatre': ['1922 in music'], 'september': ['1922 in music'], 'ran': ['1922 in music'], 'performances': ['1922 in music'], 'august': ['1922 in music'], 'american': ['1922 in music'], 'singer': ['1922 in music'], 'actress': ['1922 in music'], 'composer': ['1922 in music'], 'june': ['1922 in music']}
        self.assertEqual(keyword_to_titles(metadata), expected_keyword_to_titles_results)
        
    def test_title_to_info(self):
        metadata = [['1922 in music', 'Gary King', 1242717698, 11576, ['music', 'the', '1922', 'january', 'first', 'may', 'orchestra', 'radio', 'october', 'and', 'for', 'paul', 'walter', 'george', 'billy', 'harry', 'you', 'march', 'april', 'production', 'opened', 'theatre', 'september', 'ran', 'performances', 'august', 'american', 'singer', 'actress', 'composer', 'june']], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185, ['wright', 'was', 'and', 'member', 'the', 'band', 'pink', 'floyd', 'all', 'but', 'one', 'playing', 'end', 'waters', 'mason', 'while', 'after', 'joined', 'barrett', 'group', 'him', 'gilmour', 'with', 'later', 'touring', 'wall', 'for', 'became', 'full', 'time', 'division', 'bell', 'sessions', 'during', 'were', 'released', 'album', 'from', 'two', 'solo', 'including', 'broken', 'live', 'part', 'lead', 'such', 'his', 'farfisa', 'hammond', 'took', 'early', 'play', 'guitar', 'piano', 'mother', 'musical', 'music', 'which', 'not', 'had', 'london', 'organ', 'through', 'first', 'that', 'vocals', 'played', 'keyboards', 'would', 'concert', 'been', 'more', 'some', 'tour', 'said', 'used', 'using']]]
        expected_title_to_info_results = {'1922 in music': {'author': 'Gary King', 'timestamp': 1242717698, 'length': 11576}, 'Richard Wright (musician)': {'author': 'RussBot', 'timestamp': 1189536295, 'length': 16185}}        
        self.assertEqual(title_to_info(metadata), expected_title_to_info_results)
        metadata = []        
        expected_title_to_info_results = {}        
        self.assertEqual(title_to_info(metadata), expected_title_to_info_results)
        metadata = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_title_to_info_results = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}       
        self.assertEqual(title_to_info(metadata), expected_title_to_info_results)

    def test_search(self):
        dictionary = {'cadogan': ['Kevin Cadogan'], 'record': ['Kevin Cadogan'], 'and': ['Kevin Cadogan'], 'the': ['Kevin Cadogan'], 'band': ['Kevin Cadogan'], 'third': ['Kevin Cadogan'], 'eye': ['Kevin Cadogan'], 'blind': ['Kevin Cadogan'], 'with': ['Kevin Cadogan'], 'from': ['Kevin Cadogan'], 'their': ['Kevin Cadogan'], 'album': ['Kevin Cadogan'], 'his': ['Kevin Cadogan'], 'jenkins': ['Kevin Cadogan'], 'recording': ['Kevin Cadogan'], 'elektra': ['Kevin Cadogan'], 'records': ['Kevin Cadogan'], 'was': ['Kevin Cadogan'], 'for': ['Kevin Cadogan'], 'california': ['Kevin Cadogan'], 'two': ['Kevin Cadogan'], 'music': ['Kevin Cadogan'], 'that': ['Kevin Cadogan'], 'have': ['Kevin Cadogan'], 'were': ['Kevin Cadogan']}
        expected_search_results = ['Kevin Cadogan']
        self.assertEqual(search('record', dictionary), expected_search_results)
        dictionary = {}
        expected_search_results = []
        self.assertEqual(search('record', dictionary), expected_search_results)
        dictionary = {'cadogan': ['Kevin Cadogan'], 'record': ['Kevin Cadogan'], 'and': ['Kevin Cadogan'], 'the': ['Kevin Cadogan'], 'band': ['Kevin Cadogan'], 'third': ['Kevin Cadogan'], 'eye': ['Kevin Cadogan'], 'blind': ['Kevin Cadogan'], 'with': ['Kevin Cadogan'], 'from': ['Kevin Cadogan'], 'their': ['Kevin Cadogan'], 'album': ['Kevin Cadogan'], 'his': ['Kevin Cadogan'], 'jenkins': ['Kevin Cadogan'], 'recording': ['Kevin Cadogan'], 'elektra': ['Kevin Cadogan'], 'records': ['Kevin Cadogan'], 'was': ['Kevin Cadogan'], 'for': ['Kevin Cadogan'], 'california': ['Kevin Cadogan'], 'two': ['Kevin Cadogan'], 'music': ['Kevin Cadogan'], 'that': ['Kevin Cadogan'], 'have': ['Kevin Cadogan'], 'were': ['Kevin Cadogan']}
        expected_search_results = []
        self.assertEqual(search('RECORD', dictionary), expected_search_results)

    def test_article_length(self):
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Endogenous cannabinoid': {'author': 'Pegship', 'timestamp': 1168971903, 'length': 26}, 'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, '2007 Bulldogs RLFC season': {'author': 'Burna Boy', 'timestamp': 1177410119, 'length': 11116}, 'Peter Brown (music industry)': {'author': 'Pegship', 'timestamp': 1240235639, 'length': 2837}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '2009 Louisiana Tech Bulldogs football team': {'author': 'Nihonjoe', 'timestamp': 1245796406, 'length': 22410}, 'Georgia Bulldogs football': {'author': 'Burna Boy', 'timestamp': 1166567889, 'length': 43718}, 'Endoglin': {'author': 'Bearcat', 'timestamp': 1212259031, 'length': 6778}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'The Mandogs': {'author': 'Mack Johnson', 'timestamp': 1205282029, 'length': 3968}, 'Georgia Bulldogs football under Robert Winston': {'author': 'jack johnson', 'timestamp': 1166046122, 'length': 1989}, 'Wildlife photography': {'author': 'Jack Johnson', 'timestamp': 1165248747, 'length': 1410}, 'Landseer (dog)': {'author': 'Bearcat', 'timestamp': 1231438650, 'length': 2006}, 'Charles McPherson (musician)': {'author': 'Bearcat', 'timestamp': 1255183865, 'length': 3007}}
        expected_article_length_results = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        self.assertEqual(article_length(70000, article_titles, title_to_info), expected_article_length_results)
        article_titles = []
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Endogenous cannabinoid': {'author': 'Pegship', 'timestamp': 1168971903, 'length': 26}, 'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, '2007 Bulldogs RLFC season': {'author': 'Burna Boy', 'timestamp': 1177410119, 'length': 11116}, 'Peter Brown (music industry)': {'author': 'Pegship', 'timestamp': 1240235639, 'length': 2837}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '2009 Louisiana Tech Bulldogs football team': {'author': 'Nihonjoe', 'timestamp': 1245796406, 'length': 22410}, 'Georgia Bulldogs football': {'author': 'Burna Boy', 'timestamp': 1166567889, 'length': 43718}, 'Endoglin': {'author': 'Bearcat', 'timestamp': 1212259031, 'length': 6778}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'The Mandogs': {'author': 'Mack Johnson', 'timestamp': 1205282029, 'length': 3968}, 'Georgia Bulldogs football under Robert Winston': {'author': 'jack johnson', 'timestamp': 1166046122, 'length': 1989}, 'Wildlife photography': {'author': 'Jack Johnson', 'timestamp': 1165248747, 'length': 1410}, 'Landseer (dog)': {'author': 'Bearcat', 'timestamp': 1231438650, 'length': 2006}, 'Charles McPherson (musician)': {'author': 'Bearcat', 'timestamp': 1255183865, 'length': 3007}}
        expected_article_length_results = []
        self.assertEqual(article_length(-70000, article_titles, title_to_info), expected_article_length_results)
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Endogenous cannabinoid': {'author': 'Pegship', 'timestamp': 1168971903, 'length': 26}, 'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, '2007 Bulldogs RLFC season': {'author': 'Burna Boy', 'timestamp': 1177410119, 'length': 11116}, 'Peter Brown (music industry)': {'author': 'Pegship', 'timestamp': 1240235639, 'length': 2837}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '2009 Louisiana Tech Bulldogs football team': {'author': 'Nihonjoe', 'timestamp': 1245796406, 'length': 22410}, 'Georgia Bulldogs football': {'author': 'Burna Boy', 'timestamp': 1166567889, 'length': 43718}, 'Endoglin': {'author': 'Bearcat', 'timestamp': 1212259031, 'length': 6778}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'The Mandogs': {'author': 'Mack Johnson', 'timestamp': 1205282029, 'length': 3968}, 'Georgia Bulldogs football under Robert Winston': {'author': 'jack johnson', 'timestamp': 1166046122, 'length': 1989}, 'Wildlife photography': {'author': 'Jack Johnson', 'timestamp': 1165248747, 'length': 1410}, 'Landseer (dog)': {'author': 'Bearcat', 'timestamp': 1231438650, 'length': 2006}, 'Charles McPherson (musician)': {'author': 'Bearcat', 'timestamp': 1255183865, 'length': 3007}}
        expected_article_length_results = []
        self.assertEqual(article_length(0, article_titles, title_to_info), expected_article_length_results)

    def test_key_by_author(self):
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Endogenous cannabinoid': {'author': 'Pegship', 'timestamp': 1168971903, 'length': 26}, 'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, '2007 Bulldogs RLFC season': {'author': 'Burna Boy', 'timestamp': 1177410119, 'length': 11116}, 'Peter Brown (music industry)': {'author': 'Pegship', 'timestamp': 1240235639, 'length': 2837}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '2009 Louisiana Tech Bulldogs football team': {'author': 'Nihonjoe', 'timestamp': 1245796406, 'length': 22410}, 'Georgia Bulldogs football': {'author': 'Burna Boy', 'timestamp': 1166567889, 'length': 43718}, 'Endoglin': {'author': 'Bearcat', 'timestamp': 1212259031, 'length': 6778}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'The Mandogs': {'author': 'Mack Johnson', 'timestamp': 1205282029, 'length': 3968}, 'Georgia Bulldogs football under Robert Winston': {'author': 'jack johnson', 'timestamp': 1166046122, 'length': 1989}, 'Wildlife photography': {'author': 'Jack Johnson', 'timestamp': 1165248747, 'length': 1410}, 'Landseer (dog)': {'author': 'Bearcat', 'timestamp': 1231438650, 'length': 2006}, 'Charles McPherson (musician)': {'author': 'Bearcat', 'timestamp': 1255183865, 'length': 3007}}
        expected_key_by_author_results = {'Pegship': ['Black dog (ghost)']}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_key_by_author_results)
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {}
        expected_key_by_author_results = {}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_key_by_author_results)
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {}
        expected_key_by_author_results = {}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_key_by_author_results)

    
    def test_filter_to_author(self):
        author = 'jack johnson'
        article_titles =  ['Noise (music)', 'Kevin Cadogan', 'Rock music', 'Annie (musical)']        
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_filter_to_author_results = ['Noise (music)', 'Annie (musical)']
        self.assertEqual(filter_to_author(author, article_titles, title_to_info), expected_filter_to_author_results)
        author = 'habeebah dawodu'
        article_titles =  ['Noise (music)', 'Kevin Cadogan', 'Rock music', 'Annie (musical)']        
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_filter_to_author_results = []
        self.assertEqual(filter_to_author(author, article_titles, title_to_info), expected_filter_to_author_results)
        author = 'jack johnson'
        article_titles =  []        
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_filter_to_author_results = []
        self.assertEqual(filter_to_author(author, article_titles, title_to_info), expected_filter_to_author_results)


    def test_filter_out(self):
        keyword = 'recording'
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_filter_out_results = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        self.assertEqual(filter_out(keyword, article_titles, title_to_info), expected_filter_out_results)
        keyword = 'recording'
        article_titles = []
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_filter_out_results = []
        self.assertEqual(filter_out(keyword, article_titles, title_to_info), expected_filter_out_results)
        keyword = ''
        article_titles = []
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_filter_out_results = []
        self.assertEqual(filter_out(keyword, article_titles, title_to_info), expected_filter_out_results)

    def test_articles_from_year(self):
        year = 2008
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_articles_from_year_results = []        
        self.assertEqual(articles_from_year(year, article_titles, title_to_info), expected_articles_from_year_results)
        year = 2007
        article_titles =  ['Noise (music)', 'Kevin Cadogan', 'Rock music', 'Annie (musical)']        
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_articles_from_year_results = ['Noise (music)']       
        self.assertEqual(articles_from_year(year, article_titles, title_to_info), expected_articles_from_year_results)
        year = 1567
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        title_to_info = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}}
        expected_articles_from_year_results = []        
        self.assertEqual(articles_from_year(year, article_titles, title_to_info), expected_articles_from_year_results)


    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_test(self, input_mock):
        keyword = 'music'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\n"
        #self.maxDiff = None
        self.assertEqual(output, expected)
        
    @patch('builtins.input')
    def test_article_length_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        advanced_response = 70000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_key_by_author_test(self, input_mock):
        keyword = 'love'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'RussBot': ['2009 in music']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_filter_to_author(self, input_mock):
        keyword = 'music'
        advanced_option = 3
        advanced_response = 'jack johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'Noise (music)', '1986 in music', 'Tim Arnold (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'Traditional Thai musical instruments', '2006 in music']\n"

    @patch('builtins.input')
    def test_filter_out_test(self, input_mock):
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'love'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', 'Rock music', 'Lights (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_articles_from_year_test(self, input_mock):
        keyword = 'music'
        advanced_option = 5
        advanced_response = 2007

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', 'Tim Arnold (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Alex Turner (musician)', 'List of gospel musicians', 'Traditional Thai musical instruments', '2006 in music', '2007 in music']\n"

        self.assertEqual(output, expected)


 #python3 search_tests.py
        #python3 search_tests.py
# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
