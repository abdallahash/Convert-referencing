from PIL import Image, ImageTk 
import e_journal
import tkinter as tk 
from tkinter import ttk, StringVar, IntVar 


frame = tk.Tk()
frame.geometry('750x500')
frame.title("Convert Referencing")

source_frame = ttk.Frame(frame, height=20, width=40)
source_frame.grid(column=1, row=1)
source_frame['borderwidth']= 10
#source_frame['relief'] = 'groove'
source_frame['padding'] = 5

new_style_frame = ttk.Frame(frame)
new_style_frame.grid(column=1, row=3)
new_style_frame['relief'] = "groove"
new_style_frame['padding'] = 5

s_type = StringVar() 
source_type = ttk.Combobox(source_frame, textvariable = s_type)
source_type['values'] = ("Journal", "E_Journal", "Book")
source_type.state(['readonly'])
source_type.grid(column=0, row=0)

ref_format = StringVar()
refernce_format = ttk.Combobox(source_frame, textvariable= ref_format)
refernce_format['values'] = ("Harverd", "IEEE", "APA")
refernce_format.state(['readonly'])
refernce_format.grid(column=1, row=0)

new_style = StringVar()
new_reference_style = ttk.Combobox(new_style_frame, textvariable = new_style)
new_reference_style['values'] = ("Harverd", "APA")
new_reference_style.state(['readonly'])
new_reference_style.grid(column=0) 

source_spects = tk.Label(text="Sourse specification")
source_spects.grid(column=0,row=1)

sourse_reference = tk.Label(text="Sourse reference")
sourse_reference.grid(column=0,row=2)

new_style_label = tk.Label(frame,text="New reference style")
new_style_label.grid(column=0, row=3)

sourse_entry = tk.Entry(width = 100)
sourse_entry.grid(column=1, row=2)

class source_Journal(object):
    def __init__(self, Author, title, subtitle, volume, page, year):
        self.Author = Author
        self.title = title
        self.subtitle = subtitle
        self.volume = volume 
        self.page = page 
        self.year = year 
        #self.link= link 
    @classmethod
    def IEEE_journal(cls, reference):
        variabls = volume = Author = year = page = subtitle = title = ''
        #variable_list = []
        Author, title, variabls = reference.split('\"')
        title.replace("," , "")
        if 'vol' in variabls:
            subtitle, volume, page, year = variabls.split(',')
        else:

            subtitle, year, page = variabls.split(',')
        return cls(Author, title, subtitle, volume, page, year)
    


        """
        for index in variable_list:
            if(('pp' or'PP') in index):
                page = index 
            elif (len(index) == 5 and index[1:].isdigit()):
                year = index
            elif (('vol'or 'Vol') in index):
                volume = index 
            else:
                subtitle = index
        return cls(Author, title, subtitle, year, volume, page)
        """
                
        

"""
    def Journal(self, reference):
        reference_split = []
        reference_split= reference.split('”')
        Author = reference_split[0]
        title = reference_split[1]
        varialbls = reference_split[2]
        varialbls_list = varialbls.split(',')
        reference_split.remove(varialbls)
        volume = ''
        for index in varialbls_list:
            if(('pp' or'PP') in index):
                page = index #for index in others_list:
            elif (len(index) == 5 and index[1:].isdigit()):
                year = index
            elif (('vol'or 'Vol') in index):
                volume = index 
            else:
                subtitle = index
        #journal_dict=[Author, title, subtitle, year , volume, page]
        return Author, title, subtitle, year , volume, page

class source_Ejournal(source_Journal):
    def __init__(self, Author, title, subtitle, volume, page, year, link, no, form, accessdate):
        super().__init__(Author,title, subtitle, volume, page, year)
        self.link = link 
        self.no = no
        self.form = form 
        self.accessdate= accessdate 
    @classmethod
    def IEEE_Ejournal(cls, source):
        Author, title, other_variable = source.split("\"")
"""   

    
    

class new_journal(source_Journal):
    def Harvert_Journal(self):
        return "{}. {}. {}. {}. {}. {}".format(self.Author, e_journal.new_Ejournal.Year_Only(self.year), self.title, self.subtitle, self.volume, self.page)

    def APA_Journal(self):
        return "{}.{}.{}.{},{},{}".format(e_journal.new_Ejournal.Name_in_harverd(self.Author),e_journal.new_Ejournal.Year_Only(self.year),self.title, self.subtitle,self.volume, self.page)

def convert_majec():
    text_answer = tk.Text(master = frame, height=10, width=70)
    text_answer.grid(column=1, row=4)
    #sourse_type = input("For Journal Enter 1: \nFor E-Journal Enter 2: ")
    referance_1 = sourse_entry.get()
    if (s_type.get() == "Journal" and ref_format.get() == "IEEE"):

        if new_style.get() == "Harverd":
            
            final_refernce = source_Journal.IEEE_journal(referance_1)
            journal_in_harverd = new_journal.Harvert_Journal(final_refernce)
            text_answer.insert(tk.END, journal_in_harverd)
        
        elif new_style.get() == "APA":
            
            final_refernce = source_Journal.IEEE_journal(referance_1)
            journal_in_APA = new_journal.APA_Journal(final_refernce)
            text_answer.insert(tk.END, journal_in_APA)
    
    elif (s_type.get() == "E_Journal" and ref_format.get() == "IEEE"):
        
        if new_style.get() == "Harverd":

            final_refernce = e_journal.source_Ejournal.IEEE_Ejournal(referance_1)
            e_journal_in_harverd = e_journal.new_Ejournal.harverd_format(final_refernce)
            text_answer.insert(tk.END, e_journal_in_harverd)

        elif new_style.get() == "APA":

            final_refernce = e_journal.source_Ejournal.IEEE_Ejournal(referance_1)
            e_journal_in_APA = e_journal.new_Ejournal.APA_format(final_refernce)
            text_answer.insert(tk.END, e_journal_in_APA)
    else:
        text_answer.insert(tk.END, 'The Specification you entered are invalid')

convert_button = tk.Button(new_style_frame, text="Convert", command= convert_majec)
convert_button.grid(column=1, row = 0)

image = Image.open("/Users/Dell/Downloads/Referencing_Wordle.png")


image.thumbnail((150, 150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

#IEEE  reference = "Rattanawong, W., H. S. Masood and P. Lovenitti, ” A volumetric approach to part-build orient ations in rapid prototyping,” Journal of Materials Procesing Technology, 2001, pp. 348-353"
#Harverd  Rattanawong, W., H. S. Masood and P. Lovenitti, .  2001.  A volumetric approach to part-build orient ations in rapid prototyping,.  Journal of Materials Procesing Technology.pp. 348-353
#H. K. Edwards and V. Sridhar, "Analysis of software requirements engineering exercises in a global virtual team setup," Journal of Global Information Management, vol. 13, no. 2, p. 21+, April-June 2005. [Online]. Available: Academic OneFile, http://find.galegroup.com. [Accessed May 31, 2005].


frame.mainloop()


#<script src="https://anvil.works/embed.js" async></script>
#<iframe style="width:100%;" data-anvil-embed src="https://KEDNZQLJGKJVQHHK.anvil.app"></iframe>