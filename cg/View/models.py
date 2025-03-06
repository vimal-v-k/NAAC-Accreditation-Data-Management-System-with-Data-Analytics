from django.db import models

class Details3_1_1(models.Model):
    Name_of_the_research_project_endowment = models.CharField(max_length=200)
    Name_of_the_Principal_Investigator_Co_investigator = models.CharField(max_length=200)
    Department_of_Principal_Investigator = models.CharField(max_length=200)
    Year_of_Award = models.DateField(default=0)
    Amount_Sanctioned = models.IntegerField(default=0)
    Duration_of_the_project = models.IntegerField(default=0)
    Name_of_the_Funding_Agency = models.CharField(max_length=200)
    Government_non_Government = models.CharField(max_length=20, choices=(("Government", "Government"), ("Non-Government", "Non-Government")))
    Uploaded_by = models.CharField(max_length=50)

class Details3_2_2(models.Model):
    Year = models.DateField(default=None)
    Name_of_the_workshop_seminar_conference = models.CharField(max_length=200)
    Number_of_Participants = models.IntegerField(default=0)
    Date_From = models.DateField(default=None)
    Date_To = models.DateField(default=None)
    radiobutton322 = models.CharField(max_length=50,default=None ,choices=(("Research Methodology", "Research Methodology"), ("Intellectual Property Rights (IPR)", "Intellectual Property Rights (IPR)"), ("Entrepreneurship","Entrepreneurship")))
    Link_to_the_Activity_report_on_the_website = models.URLField(default=None)
    Uploaded_by = models.CharField(max_length=50)

class Details3_3_1(models.Model):
    Title_of_paper = models.CharField(max_length=200)
    Name_of_the_authors = models.CharField(max_length=200)
    Department_of_the_teacher = models.CharField(max_length=60, choices=(("Automobile Engineering", "Automobile Engineering"), ("Basic Science and Humanities", "Basic Science and Humanities"), ("Civil Engineering", "Civil Engineering"), ("Computer Science & Engineering", "Computer Science & Engineering"), ("Electrical & Electronics Engineering", "Electrical & Electronics Engineering"), ("Electronics & Communication Engineering", "Electronics & Communication Engineering"), ("Mechanical Engineering", "Mechanical Engineering")))
    Name_of_journal = models.CharField(max_length=200)
    Year_of_publication = models.DateField(default=0)
    ISSN_number = models.IntegerField(default=0)
    Link_to_website_of_the_Journal = models.URLField(default=None)
    Link_to_article_paper_abstract_of_the_article = models.URLField(default=None)
    Is_it_listed_in_UGC_Care_list = models.CharField(max_length=5, choices=(("YES", "YES"), ("NO", "NO")))
    Uploaded_by = models.CharField(max_length=50)

class Details3_3_2(models.Model):
    Name_of_the_teacher = models.CharField(max_length=50)
    Title_of_the_book_chapters_published = models.CharField(max_length=200)
    Title_of_the_paper = models.CharField(max_length=100)
    Title_of_the_proceedings_of_the_conference = models.CharField(max_length=200)
    Name_of_the_conference = models.CharField(max_length=200)
    national_international = models.CharField(max_length=50,choices=(("National","National"),("International","International")))
    Year_of_publications = models.DateField(default=None)
    ISBN_number_of_the_proceeding = models.IntegerField(default=0)
    Affiliating_Institute_at_the_time_of_publication = models.CharField(max_length=200)
    Name_of_the_publisher=models.CharField(max_length=100)
    Uploaded_by = models.CharField(max_length=50)

class Details3_4_3(models.Model):
    Name_of_the_activity = models.CharField(max_length=200)
    Organising_unit_agency_collaborating_agency = models.CharField(max_length=200)
    Name_of_the_scheme = models.CharField(max_length=60)
    Year_of_the_activity = models.DateField(default=None)
    Uploaded_by = models.CharField(max_length=50)


class Details3_5_1(models.Model):
    Name_of_the_MoU_Collaboration_linkage = models.CharField(max_length=200)
    Name_of_the_collaborating_agency_institution_industry_corporate_house_with_whom_the_MoU_collaboration_linkage_is_made_with_contact_details = models.CharField(max_length=60)
    Year_of_signing_MoU_collaboration_linkage = models.DateField(default=None)
    radiobutton3_5_1 = models.CharField(max_length=50,default=None,choices=(("1 year","1 year"),("2 year","2 year"),("3 year","3 year"),("4 year","4 year"),("5 year","5 year")))
    List_the_actual_activities_under_each_MOU_and_web_inks_year_wise = models.CharField(max_length=200)
    Link_to_the_relevant_document = models.CharField(max_length=200)
    Uploaded_by = models.CharField(max_length=50)

class Citations(models.Model):
    Name = models.CharField(max_length=200,default=None)
    Cemail = models.CharField(max_length=50,default=None)
    Citations = models.IntegerField(default=0)
    h_index = models.IntegerField(default=0)
    i10_index =  models.IntegerField(default=0)
    profile_link = models.CharField(max_length=200)
    Department= models.CharField(max_length=60, default=None,choices=(("Automobile Engineering", "Automobile Engineering"), ("Basic Science and Humanities", "Basic Science and Humanities"), ("Civil Engineering", "Civil Engineering"), ("Computer Science & Engineering", "Computer Science & Engineering"), ("Electrical & Electronics Engineering", "Electrical & Electronics Engineering"), ("Electronics & Communication Engineering", "Electronics & Communication Engineering"), ("Mechanical Engineering", "Mechanical Engineering")))
    year= models.CharField(max_length=60, default=None,choices=(("2018", "2018"), ("2019", "2019"), ("2020", "2020"), ("2021", "2021"), ("2022", "2022"), ("2023", "2023")))

