import random
import re

class NamingAlgo:
    
    def DropAndCombine(word1, word2, name_length):
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        index1 = random.randint(0, len_word1-1)
        index2 = random.randint(0, len_word2-1)
        
        letter1 = word1[index1]
        letter2 = word2[index2]
        
        result_1 = word1.replace(letter1, '')
        result_2 = word2.replace(letter2, '')
        result = result_1 + result_2
        result = re.sub('[^A-Za-z0-9]+', '', result)
        
        return result[:name_length]

    #abstract
    def CombineAndDrop(word1, word2, name_length):
        result = word1 + word2
        result = re.sub('[^A-Za-z0-9]+', '', result)
        word_length = len(result)
        
        index1 = random.randint(0, word_length-1)
        index2 =  random.randint(0, word_length-1)
        
        letter1 = result[index1]
        letter2 = result[index2]
        
        result = result.replace(letter1, '')
        result = result.replace(letter2, '')
        
        return result[:name_length]

    #descriptive
    def JustCombine(word1, word2, name_length):
        result = word1 + word2
        result = re.sub('[^A-Za-z0-9]+', '', result)
        
        return result[:name_length]

    #abstract
    def Shuffle(word1, word2, name_length):
        word = word1+word2
        word = re.sub('[^A-Za-z0-9]+', '', word)
        
        l = list(word)
        random.shuffle(l)
        result = ''.join(l)
        
        return result[:name_length]
    
    def AlgoEntry(phrases, app_description, name_length):
        result_names= []
        
        for phrase in phrases:
            result_1 = NamingAlgo.DropAndCombine(phrase, app_description[0], name_length)
            if result_1 not in result_names:
                result_names.append(result_1)
            result_1_variant = NamingAlgo.DropAndCombine(app_description[0],phrase, name_length)
            if result_1_variant not in result_names:
                result_names.append(result_1_variant)
            
            result_2 = NamingAlgo.JustCombine(phrase, app_description[0], name_length)
            if result_2 not in result_names:
                result_names.append(result_2)
            result_2_variant = NamingAlgo.JustCombine(app_description[0],phrase, name_length)
            if result_2_variant not in result_names:
                result_names.append(result_2_variant)
            result_3 = NamingAlgo.CombineAndDrop(phrase, app_description[0], name_length)
            if result_3 not in result_names:
                result_names.append(result_3)
            result_3_variant = NamingAlgo.CombineAndDrop(app_description[0],phrase, name_length)
            if result_3_variant not in result_names:
                result_names.append(result_3_variant)
            result_4 = NamingAlgo.Shuffle(phrase, app_description[0], name_length)
            if result_4 not in result_names:
                result_names.append(result_4)
            result_4_variant = NamingAlgo.Shuffle(app_description[0],phrase, name_length)
            if result_4_variant not in result_names:
                result_names.append(result_4_variant)
        
        without_empty_string =  [string for string in result_names if string != ""]
    
        return [string for string in without_empty_string if len(string) >= 3]