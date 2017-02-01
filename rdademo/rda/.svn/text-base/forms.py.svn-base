from django import forms

# Work
class WorkForm(forms.Form):
    # Core
    title = forms.CharField(max_length=255, label='Title of the Work', help_text='FRBR 4.2.1 FRAD 5.2')
    #preferred_title = forms.CharField(max_length=255, label='Preferred Title for the Work', help_text='FRBR 4.2.1 FRAD 5.2') #
    #variant_title = forms.CharField(max_length=255, label='Variant Title for the Work', help_text='FRBR 4.2.1 FRAD 5.2') #
    date = forms.CharField(max_length=255, label='Date of Work', help_text='FRBR 4.2.3 FRAD 4.4')
    origin = forms.CharField(max_length=255, label='Place of Origin of the Work', help_text='FRAD 4.4')
    form = forms.CharField(max_length=255, label='Form of Work', help_text='FRBR 4.2.2 FRAD 4.4')
    other = forms.CharField(max_length=255, label='Other Distinguishing Characteristic of the Work', help_text='FRBR 4.2.4 FRAD 4.4')
    identifier = forms.CharField(max_length=255, label='Identifier for the Work', help_text='FRAD 5.2')
    signatory = forms.CharField(max_length=255, label='Signatory to a Treaty, etc', help_text='')
    key = forms.CharField(max_length=255, label='Key', help_text='FRBR 4.2.12 FRAD 4.4')
    designation = forms.CharField(max_length=255, label='Numeric Designation of a Musical Work', help_text='FRBR 4.2.9 FRAD 4.4')
    #medium = forms.CharField(max_length=255, label='Medium of Performance', help_text='FRBR 4.2.8 FRAD 4.4')
    
    # Enhanced
    nature = forms.CharField(max_length=255, label='Nature of the Content', help_text='FRBR 4.2.2. 4.3.25')
    coverage = forms.CharField(max_length=255, label='Coverage of the Content', help_text='')
    organization = forms.CharField(max_length=255, label='System of Organization', help_text='')
    audience = forms.CharField(max_length=255, label='Intended Audience', help_text='FRBR 4.2.6')
    history = forms.CharField(max_length=255, label='History of the Work', help_text='FRAD 4.4')
    epoch = forms.CharField(max_length=255, label='Epoch', help_text='')
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='')
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='')
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguer\'s Note', help_text='')
    status_of_id = forms.CharField(max_length=255, label='Status of Identification', help_text='') 

    # Special
    academic_degree = forms.CharField(max_length=255, label='Academic Degree', help_text='') 
    granting_institution = forms.CharField(max_length=255, label='Granting Institution or Faculty', help_text='') 
    year_granted = forms.CharField(max_length=255, label='Year Degree Granted', help_text='') 
    longitude = forms.CharField(max_length=255, label='Longitude', help_text='FRBR 4.2.11') 
    latitude = forms.CharField(max_length=255, label='Latitude', help_text='FRBR 4.2.11') 
    coord_pairs = forms.CharField(max_length=255, label='Strings of Coordinate Pairs', help_text='FRBR 4.2.11') 
    right_asc_decl = forms.CharField(max_length=255, label='Right Ascension and Declination', help_text='FRBR 4.2.11') 
    equinox = forms.CharField(max_length=255, label='Equinox', help_text='FRBR 4.2.12') 

# Expression

class ExpressionForm(forms.Form):
    
    # Core
    date = forms.CharField(max_length=255, label='Date of Expression', help_text='FRBR 4.4.3 FRAD 4.5')
    language_expression = forms.CharField(max_length=255, label='Language of Expression', help_text='FRBR 4.3.4 FRAD 4.5')
    other = forms.CharField(max_length=255, label='Other Distinguishing Characteristic of the Expression', help_text='FRBR 4.3.4 FRAD 4.5')
    identifier = forms.CharField(max_length=255, label='Identifier for the Expression', help_text='FRAD 5.2')
    content_type = forms.CharField(max_length=255, label='Content Type', help_text='FRBR 4.3.2 FRAD 4.5')
    
    # Enhanced
    credit = forms.CharField(max_length=255, label='Artistic and/or Technical Credit', help_text='')
    duration = forms.CharField(max_length=255, label='Duration', help_text='FRBR 4.3.8')
    language_content = forms.CharField(max_length=255, label='Language of the Content', help_text='FRBR 4.3.4')
    place_and_date_of_capture = forms.CharField(max_length=255, label='Place and Date of Capture', help_text='')
    accessibility_content = forms.CharField(max_length=255, label='Accessibility Content', help_text='')
    illustrative_content = forms.CharField(max_length=255, label='Illustrative Content', help_text='')
    form_of_notation = forms.CharField(max_length=255, label='Form of Notation', help_text='')
    script = forms.CharField(max_length=255, label='Script', help_text='FRBR 7.13.2.3')
    form_of_tactile_notation = forms.CharField(max_length=255, label='Form of Tactile Notation', help_text='')
    summarization = forms.CharField(max_length=255, label='Summarization of the Content', help_text='FRBR 4.3.9')
    supplementary_content = forms.CharField(max_length=255, label='Supplementary Content', help_text='')
    source_consulted = forms.CharField(max_length=255, label='Source Consulted', help_text='')
    status_of_identification = forms.CharField(max_length=255, label='Status of Identification', help_text='')
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='')
    awards = forms.CharField(max_length=255, label='Awards', help_text='FRBR 4.3.11')
    
    # Special
    aspect_ratio = forms.CharField(max_length=255, label='Aspect Ratio', help_text='FRBR 4.4.34') 
    scale = forms.CharField(max_length=255, label='Scale', help_text='') 
    additional_scale_information = forms.CharField(max_length=255, label='Additional Scale Information', help_text='FRBR 4.3.18')
    format_of_notated_music = forms.CharField(max_length=255, label='Format of Notated Music', help_text='FRBR 4.3.16')
    sound_content = forms.CharField(max_length=255, label='Sound Content', help_text='')
    performer_narrator_or_presenter = forms.CharField(max_length=255, label='Performer, Narrator, and/or Presenter', help_text='')
    medium_of_performance = forms.CharField(max_length=255, label='Medium of Performance of Musical Content', help_text='FRBR 4.3.17')
    colour_content = forms.CharField(max_length=255, label='Colour Content', help_text='FRAD 4.5')
    colour_content_of_resource_for_visual_impairments = forms.CharField(max_length=255, label='Colour Content of Resource Designed for Persons with Visual Impairments', help_text='FRBR 4.4.6') 
    other_details  = forms.CharField(max_length=255, label='Other Details of Cartographic Content', help_text='FRBR 4.2.11, 4.3.18, 4.3.19-4.3.24')
    projection = forms.CharField(max_length=255, label='Projection of Cartographic Content', help_text='FRBR 4.3.19')

# Manifestation
class ManifestationForm(forms.Form):
    
    # Core
    title = forms.CharField(max_length=255, label='Title', help_text='FRBR 4.4.1')
    date = forms.CharField(max_length=255, label='Copyright Date', help_text='FRBR 4.4.6')
    carrier_type = forms.CharField(max_length=255, label='Carrier Type', help_text='FRBR 4.4.9')
    extent = forms.CharField(max_length=255, label='Extent', help_text='FRBR 4.3.8 4.4.10')
    num_of_serials = forms.CharField(max_length=255, label='Numbering of Serials', help_text='FRBR 4.4.23')
    identifier = forms.CharField(max_length=255, label='Identifier for the Manifestation', help_text='FRBR 4.4.14 4.5.2')
    statement_responsibility = forms.CharField(max_length=255, label='Statement of Responsibility', help_text='FRBR 4.4.2')
    statement_series = forms.CharField(max_length=255, label='Series Statement', help_text='FRBR 4.4.8')
    statement_edition = forms.CharField(max_length=255, label='Edition Statement', help_text='FRBR 4.4.3')
    statement_publication = forms.CharField(max_length=255, label='Publication Statement', help_text='')
    statement_manufacture = forms.CharField(max_length=255, label='Manufacture Statement', help_text='')
    statement_distribution = forms.CharField(max_length=255, label='Distribution Statement', help_text='')
    
    # Enhanced
    mediatype = forms.CharField(max_length=255, label='Media Type', help_text='') 
    dimensions = forms.CharField(max_length=255, label='Dimensions', help_text='FRBR 4.4.13')
    resource_locator = forms.CharField(max_length=255, label='Uniform Resource Locator', help_text='FRBR 4.4.36') 
    citation = forms.CharField(max_length=255, label='Preferred Citation', help_text='') 
    note = forms.CharField(max_length=255, label='Note', help_text='') 
    production_statement = forms.CharField(max_length=255, label='Production Statement', help_text='')
    restrictions_on_access = forms.CharField(max_length=255, label='Restrictions on Access', help_text='FRBR 4.4.17')
    restrictions_on_use = forms.CharField(max_length=255, label='Restrictions on Use', help_text='FRBR 4.4.17')
    contact = forms.CharField(max_length=255, label='Contact Information', help_text='FRBR 4.4.15')
    terms = forms.CharField(max_length=255, label='Terms of Availability', help_text='FRBR 4.4.16')
    
    # Special
    mode = forms.CharField(max_length=255, label='Mode of Issuance', help_text='') 
    frequency = forms.CharField(max_length=255, label='Frequency', help_text='FRBR 4.3.15') 
    format = forms.CharField(max_length=255, label='Book Format', help_text='FRBR 4.4.20') 
    font_size = forms.CharField(max_length=255, label='Font Size', help_text='FRBR 4.4.20') 
    reduction_ratio = forms.CharField(max_length=255, label='Reduction Ratio', help_text='FRBR 4.4.31') 
    polarity = forms.CharField(max_length=255, label='Polarity', help_text='FRBR 4.4.32') 
    mount = forms.CharField(max_length=255, label='Mount', help_text='') 
    production_method = forms.CharField(max_length=255, label='Production Method', help_text='') 
    layout = forms.CharField(max_length=255, label='Layout', help_text='') 
    base_material = forms.CharField(max_length=255, label='Base Material', help_text='FRBR 4.4.11') 
    applied_material = forms.CharField(max_length=255, label='Applied Material', help_text='FRBR 4.4.11') 
    projection_characteristic = forms.CharField(max_length=255, label='Projection Characteristic of Motion Picture Film', help_text='') 
    generation = forms.CharField(max_length=255, label='Generation', help_text='') 
    video_characteristic = forms.CharField(max_length=255, label='Video Characteristic', help_text='') 
    digitalfile_characteristic = forms.CharField(max_length=255, label='Digital File Characteristic', help_text='') 
    sound_characteristic = forms.CharField(max_length=255, label='Sound Characteristic', help_text='') 
    sound_content = forms.CharField(max_length=255, label='Sound Content', help_text='') 
    equipment = forms.CharField(max_length=255, label='Equipment or System Requirement', help_text='FRBR 4.4.35') 

# Item
class ItemForm(forms.Form):

    # Core
    
    # Enhanced
    extent = forms.CharField(max_length=255, label='Extent', help_text='FRBR 4.4.10') 
    contact = forms.CharField(max_length=255, label='Contact Information', help_text='') 
    citation = forms.CharField(max_length=255, label='Preferred Citation', help_text='') 
    resource_locator = forms.CharField(max_length=255, label='Uniform Resource Locator', help_text='') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Item', help_text='FRBR 4.5.1') 
    note = forms.CharField(max_length=255, label='Note', help_text='') 
    restrictions_on_access= forms.CharField(max_length=255, label='Restrictions on Access', help_text='FNBR 4.5.9') 
    restrictions_on_use = forms.CharField(max_length=255, label='Restrictions on Use', help_text='FNBR 4.5.9') 
    dimensions = forms.CharField(max_length=255, label='Dimensions', help_text='FRBRR 4.4.13') 
    
    # Special
    history = forms.CharField(max_length=255, label='Custodial History of Item', help_text='FRBR 4.5.3') 
    source = forms.CharField(max_length=255, label='Immediate Source of Acquisition of Item', help_text='FRBR 4.5.3') 
    characteristics = forms.CharField(max_length=255, label='Item-Specific Carrier Characteristic', help_text='FRBR 4.5.6') 
    
# Person
class PersonForm(forms.Form):
    
    # Core
    name = forms.CharField(max_length=255, label='Name of the Person', help_text='FRBR 4.6.1 FRAD 5.2') 
    fullername = forms.CharField(max_length=255, label='Fuller Form of Name', help_text='FRBR 4.6.1 FRAD 4.1')
    date = forms.CharField(max_length=255, label='Date Associated with the Person', help_text='FRBR 4.6.2 FRAD 4.1') 
    title = forms.CharField(max_length=255, label='Title of the Person', help_text='FRBR 4.6.3 FRAD 4.1') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Person', help_text='FRAD 5.2') 
    activity = forms.CharField(max_length=255, label='Field of Activity of the Person', help_text='FRBR 4.6.4 FRAD 4.1')
    profession = forms.CharField(max_length=255, label='Profession or Occupation', help_text='FRBR 4.5.3') 
    other = forms.CharField(max_length=255, label='Other Designation Associated with the Person', help_text='FRBR 4.6.4 FRAD 5.2') 
        
    # Enhanced
    biographical_information = forms.CharField(max_length=255, label='Biographical Information', help_text='FRAD 4.1')
    affiliation = forms.CharField(max_length=255, label='Affiliation', help_text='FRAD 4.1')
    place_of_birth = forms.CharField(max_length=255, label='Place of Birth', help_text='FRAD 4.1')
    place_of_death = forms.CharField(max_length=255, label='Place of Death', help_text='FRAD 4.1')
    place_of_residence = forms.CharField(max_length=255, label='Place of Residence', help_text='FRAD 4.1')
    country_associated = forms.CharField(max_length=255, label='Country Associated with the Person', help_text='FRAD 4.1')
    undifferentiated_name = forms.CharField(max_length=255, label='Undifferentiated Name Indicator', help_text='') 
    address = forms.CharField(max_length=255, label='Address of the Person', help_text='FRAD 4.1') 
    note = forms.CharField(max_length=255, label='Note', help_text='') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='')
    status_of_identification = forms.CharField(max_length=255, label='Status of Identification', help_text='') 
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='')
    gender = forms.CharField(max_length=255, label='Gender', help_text='FRAD 4.1') 
    language = forms.CharField(max_length=255, label='Language of the Person', help_text='FRAD 4.1') 
    
    # Special
    
# Family
class FamilyForm(forms.Form):
    
    # Core
    name = forms.CharField(max_length=255, label='Name of the Family', help_text='FRAD 5.2') 
    type = forms.CharField(max_length=255, label='Type of Family', help_text='FRAD 4.2') 
    date = forms.CharField(max_length=255, label='Date Associated with the Family', help_text='FRAD 4.2') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Family', help_text='FRAD 5.2')
    member = forms.CharField(max_length=255, label='Prominent Members of the Family', help_text='FRAD 4.2') 
    
    # Enhanced
    title = forms.CharField(max_length=255, label='Hereditary Title', help_text='FRAD 4.2') 
    history = forms.CharField(max_length=255, label='Family History', help_text='FRAD 4.2') 
    undifferentiated_name = forms.CharField(max_length=255, label='Undifferentiated Name Indicator', help_text='')  
    note = forms.CharField(max_length=255, label='Note', help_text='') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='')
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='')
    
    # Special
    
# Corporate body
class CorporateBodyForm(forms.Form):
    
    # Core
    name = forms.CharField(max_length=255, label='Name of the Corporate Body', help_text='FRBR 4.7.1 FRAD 5.2') 
    associated = forms.CharField(max_length=255, label='Associated Insitution', help_text='') 
    date = forms.CharField(max_length=255, label='Date Associated with the Corporate Body', help_text='FRBR 4.7.4 FRAD 4.3')  
    other = forms.CharField(max_length=255, label='Other Designation Associated with the Corporate Body', help_text='FRBR 4.7.2 4.7.5 FRAD 4.3') 
    place = forms.CharField(max_length=255, label='Place Associated with the Corporate Body', help_text='FRBR 4.7.3 FRAD 4.3') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Corprate Body', help_text='FRAD 5.2')  
    
    # Enhanced
    language_expression = forms.CharField(max_length=255, label='Language of the Corporate Body', help_text='FRAD 4.3') 
    history = forms.CharField(max_length=255, label='Corporate History', help_text='FRAD 4.3')  
    activity = forms.CharField(max_length=255, label='Field of Activity of the Corporate Body', help_text='FRAD 4.3')  
    num_of_conference = forms.CharField(max_length=255, label='Number of a Conference etc.', help_text='FRBR 4.7.2') 
    undifferentiated_name = forms.CharField(max_length=255, label='Unfifferentiated Name Indicator', help_text='') 
    address = forms.CharField(max_length=255, label='Address of the Corporate Body', help_text='FRAD 4.3')  
    note = forms.CharField(max_length=255, label='Note', help_text='')  
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='')  
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='')  

    # Special

# Concept
class ConceptForm(forms.Form):
    
    # Core
    
    # Enhanced
    term = forms.CharField(max_length=255, label='Term of the Concept', help_text='FRBR 4.8.1 FRAD 5.2') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Concept', help_text='FRAD 5.2') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='') 
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='') 
    
    # Special
    
# Object
class ObjectForm(forms.Form):
    
    # Core
    
    # Enhanced
    name = forms.CharField(max_length=255, label='Name of the Object', help_text='FRBR 4.9.1 FRAD 5.2') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Object', help_text='FRAD 5.2') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='') 
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='') 
    
    
    # Special
    
# Event
class EventForm(forms.Form):
    
    # Core

    # Enhanced
    name = forms.CharField(max_length=255, label='Name of the Event', help_text='FRBR 4.10.1 FRAD 5.2') 
    identifier = forms.CharField(max_length=255, label='Identifier for the Event', help_text='FRAD 5.2') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='') 
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='') 
    
    # Special

# Place
class PlaceForm(forms.Form):
    
    # Core
    name = forms.CharField(max_length=255, label='Name of the Place', help_text='FRBR 4.11.1 FRAD 5.2') 
    
    # Enhanced
    identifier = forms.CharField(max_length=255, label='Identifier for the Place', help_text='FRAD 5.2') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='') 
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='') 
    
    # Special

# Name
class NameForm(forms.Form):
    
    # Core
    
    # Enhanced
    scope = forms.CharField(max_length=255, label='Scope of Usage', help_text='FRAD 4.12') 
    date = forms.CharField(max_length=255, label='Date of Usage', help_text='FRAD 4.12') 
    source = forms.CharField(max_length=255, label='Source Consulted', help_text='') 
    status = forms.CharField(max_length=255, label='Status of Identification', help_text='') 
    cataloguers_note = forms.CharField(max_length=255, label='Cataloguers Note', help_text='') 

    # Special
