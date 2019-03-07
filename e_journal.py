import re


class source_Ejournal:
    def __init__(self, Author, title, subtitle, volume, page, year, no, form, database, link, accessdate):
        self.Author = Author
        self.title = title
        self.subtitle = subtitle
        self.volume = volume 
        self.page = page 
        self.year = year
        self.no = no
        self.form = form
        self.database = database 
        self.link = link  
        self.accessdate= accessdate 
    @classmethod
    def IEEE_Ejournal(cls, source):
        Author= title= subtitle= volume= page= year= no= form= database= link = accessdate = ''
        if source.count('[')==2:
            form = source[source.find('['):source.find("]")+1]
            st = source.index('[')
            st+=1 
            source_slice = source[st:]
            source1 = source.replace(source_slice, '')
            
            accessdate = source_slice[source_slice.find('['):-1]
            source_slice = source_slice.split(',')
            
            if len(source_slice) == 3:
                linc = source_slice[1]
                link = linc[0:linc.index('[')]
            else:
                #print("The else statment runing")
                #print("source slice[0] >>>", source_slice[0])
                linc = source_slice[0]
                link = linc[linc.find(":")+1:linc.find("[")]
                #source_from_internet = True 

            
        Author, title, other_variable = source1.split("\"")
        title = title.replace(",","")
        variable_list = other_variable.split(',')
        year_form_database = ''
        
        for data in variable_list:
            if (volume or no or page)!= variable_list[0]:
                subtitle = variable_list[0]
            if ('vol' or 'Vol') in data:
                volume = data
            if ('no') in data:
                no = data
            if ('p.' or 'pp.') in data:
                page = data
                   
            if (volume or no or page) != variable_list[-1]:
                year = variable_list[-1]
                year = year[:-2]
                
        year_form_database = year_form_database.split('.')
        for string in year_form_database:
            if (len(year_form_database) == 3):
                year, form, database = year_form_database
            elif ('[]' in string) and len(year_form_database) == 2:
                form = string 
                year = year_form_database[0] 
      
        return cls(Author, title, subtitle, volume, page, year, no, form, database, link, accessdate)


class new_Ejournal(source_Ejournal):

    @staticmethod
    def Year_Only(years):
            # self.year = "March 2009" harverd format only want the year (2009)
            year_only = re.findall('\d+', years)[0]
            year_only = "({})".format(year_only)
            return year_only

    @staticmethod
    def volume_in_harverd(no, volume):
            #the volume and no(issue) are seprated here we want to join them in one string --> volume(no)
            issue = real_vol = ''
            if (no != '') and (volume != ''):
                issue = re.findall('\d+', no)[0]
                Har_volume = re.findall('\d+', volume)[0]
                real_vol = "Volume {}({})".format(Har_volume,issue)
            elif (volume != "") and (no == ""):
                Har_volume = re.findall('\d+', volume)[0]
                real_vol = "Volume {}".format(Har_volume) 
            else:
                real_vol = ""
            return real_vol

    @staticmethod
    def Name_in_harverd(Author):
            count = Author.count(",")
            if (' and ' in Author) and (count == 1):
                authors_list = Author.split(" and ")
                first_authorlist = authors_list[0].split(".")
                secound_authorlist = authors_list[1].split(".")
                first_nameonly = first_authorlist.pop(-1)
                secound_nameonly = secound_authorlist.pop(-1)
                first_harverdname = (first_nameonly+",")+(".".join(first_authorlist))
                secound_harverdname = (secound_nameonly)+(".".join(secound_authorlist))
                harverd_name = "{} and {}".format(first_harverdname, secound_harverdname) 
            elif (' and ' in Author) and (count > 1):
                harverd_name_list = []
                authors_list = Author.split(",")
                for author in authors_list:
                    if author != "":
                        namelist = author.split(".")
                        author_nameonly = namelist.pop(-1)
                        harverd_name_author = (author_nameonly+",")+(".".join(namelist))
                        harverd_name_list.append(harverd_name_author)
                         

                harverd_name = "{}, {}, and {}".format(harverd_name_list[0],harverd_name_list[1],harverd_name_list[2].replace(" and ", ""))

            elif (count ==1) and (" and " not in Author):
                author_listname = Author.split('.')
                nameonly = author_listname.pop(-1)
                harverd_name = (nameonly)+(". ".join(author_listname))

            else: 
                harverd_name = Author 
            return harverd_name
    
    def harverd_format(self):
        
        def Pages(page):
            if page != "":
                newpage = page.replace('pp' , 'p')
            else:
                newpage = page 
            return newpage
        
        

        return "{}.{}. {}. {}, {} {}, {}. Available at: {} {}".format(new_Ejournal.Name_in_harverd(self.Author),new_Ejournal.Year_Only(self.year),self.title, self.subtitle, self.form, new_Ejournal.volume_in_harverd(self.no, self.volume), Pages(self.page), self.link, self.accessdate)
    
    def APA_format(self):

        def apa_pages(page):
            if "pp." in page:
                new_apa_page = page.replace("pp.", "")
            elif "p." in page:
                new_apa_page = page.replace("p." , "")
            else:
                new_apa_page = page
            return new_apa_page

        return "{}.{}.{}.{},{},{}. Retrieved from {}".format(new_Ejournal.Name_in_harverd(self.Author), new_Ejournal.Year_Only(self.year), self.title, self.subtitle, new_Ejournal.volume_in_harverd(self.no, self.volume), apa_pages(self.page), self.link)






"""

referance_1 = input("Enter the source reference you want to convert>>> ")
final_referance = source_Ejournal.IEEE_Ejournal(referance_1)
print(final_referance.no)
print(final_referance.volume)
print(final_referance.page, " and year is ", final_referance.year)

print(new_Ejournal.harverd_format(final_referance))
"""
#print("Author: ", final_referance.Author, " \n Title : ", final_referance.title, " \n Year : ", final_referance.year, " \n Format : ", final_referance.form) 
#print(" \n Link : ", final_referance.link," \n Accessed date: ", final_referance.accessdate, "\n Subtitle : ", final_referance.subtitle)
#H. K. Edwards and V.sridhar," Analysis of software requirment," Journal Of Global Information, vol. 13, no. 2, p. 21+, April-June 2005. [Online]. Available: Acadamic OneFile, http://find####. [Accessed May 31, 2005].
#P. H. C. Eilers, A. Altun, and J. J. Goeman, "Enhancing scatterplots with smoothed densities," Bioinformatics, vol. 20, no. 5, pp. 623-628, March 2004. [Online]. Available: www.oxfordjournals.org. [Accessed Sept. 18, 2004].