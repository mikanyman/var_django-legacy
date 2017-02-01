from django.db import models

class Work(models.Model):
    # CORE
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='title of the work')
    #preferred_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='preferred title of the work')
    #variant_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='variant title of the work')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='date of the work')
    origin = models.CharField(max_length=255, blank=True, null=True, verbose_name='place of work')
    form = models.CharField(max_length=255, blank=True, null=True, verbose_name='form of work')
    other = models.CharField(max_length=255, blank=True, null=True, verbose_name='other characteristics')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier of the work')
    #medium = models.CharField(max_length=255, blank=True, null=True, verbose_name='medium of performance')
    signatory = models.CharField(max_length=255, blank=True, null=True, verbose_name='signatory to treaty')
    key = models.CharField(max_length=255, blank=True, null=True, verbose_name='key')
    designation = models.CharField(max_length=255, blank=True, null=True, verbose_name='numeric designation of a musical work')
    
    # ENHANCED
    nature = models.CharField(max_length=255, blank=True, null=True, verbose_name='nature of the content')
    coverage = models.CharField(max_length=255, blank=True, null=True, verbose_name='coverage of the content')
    organization = models.CharField(max_length=255, blank=True, null=True, verbose_name='system of organization')
    audience = models.CharField(max_length=255, blank=True, null=True, verbose_name='intended audience')
    history = models.CharField(max_length=255, blank=True, null=True, verbose_name='history of the work')
    epoch = models.CharField(max_length=255, blank=True, null=True, verbose_name='epoch')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    status_of_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of id')
    
    # SPECIAL
    academic_degree = models.CharField(max_length=255, blank=True, null=True, verbose_name='academic degree')
    granting_institution = models.CharField(max_length=255, blank=True, null=True, verbose_name='granting insititution')
    year_granted = models.CharField(max_length=255, blank=True, null=True, verbose_name='year granted')
    longitude = models.CharField(max_length=255, blank=True, null=True, verbose_name='longitude')
    latitude = models.CharField(max_length=255, blank=True, null=True, verbose_name='latitude')
    coord_pairs = models.CharField(max_length=255, blank=True, null=True, verbose_name='coordinate pairs')
    right_asc_decl = models.CharField(max_length=255, blank=True, null=True, verbose_name='right asc decl')
    equinox = models.CharField(max_length=255, blank=True, null=True, verbose_name='equinox')
    
    
    # Relations
    expression_of_work = models.ManyToManyField('Expression', through='ExpressionOfWork', related_name='Work_expression_of_work')
    manifestation_of_work = models.ManyToManyField('Manifestation', through='ManifestationOfWork', related_name='Manifestation_manifestation_of_work')
    creator_person = models.ManyToManyField('Person', through='Creator', related_name='Work_creator_person')
    creator_family = models.ManyToManyField('Family', through='Creator', related_name='Work_creator_family')
    creator_corporate_body = models.ManyToManyField('CorporateBody', through='Creator', related_name='Work_creator_corporate_body')
    other_person_associated_with_a_work = models.ManyToManyField('Person', through='OtherActorAssociatedWithAWork', related_name='Work_other_person_associated_with_a_work')
    other_family_associated_with_a_work = models.ManyToManyField('Family', through='OtherActorAssociatedWithAWork', related_name='Work_other_family_associated_with_a_work')
    other_corporate_body_associated_with_a_work = models.ManyToManyField('CorporateBody', through='OtherActorAssociatedWithAWork', related_name='Work_other_corporate_body_associated_with_a_work')
    related_work = models.ManyToManyField('Work', through='RelatedWork', related_name='Work_related_work')
    
    def __unicode__(self):
        return self.title

class Expression(models.Model):
    # CORE
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='date of expression')
    language_expression = models.CharField(max_length=255, blank=True, null=True, verbose_name='language of expression')
    other = models.CharField(max_length=255, blank=True, null=True, verbose_name='other distinguishing characteristics of the expression')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier of the expression')
    content_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='content type')
    
    # ENHANCED
    credit = models.CharField(max_length=255, blank=True, null=True, verbose_name='artistic or technical credit')
    duration = models.CharField(max_length=255, blank=True, null=True, verbose_name='duration')
    language_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='language of the content')
    place_and_date_of_capture = models.CharField(max_length=255, blank=True, null=True, verbose_name='place and date of the capture')
    accessibility_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='accessibility content')
    illustrative_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='illustrative content')
    form_of_notation = models.CharField(max_length=255, blank=True, null=True, verbose_name='form of notation')
    script = models.CharField(max_length=255, blank=True, null=True, verbose_name='script')
    form_of_tactile_notation = models.CharField(max_length=255, blank=True, null=True, verbose_name='form_of_tactile_notation')
    summarization = models.CharField(max_length=255, blank=True, null=True, verbose_name='summarization of the content')
    supplementary_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='supplementary content')
    source_consulted = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status_of_identification = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    awards = models.CharField(max_length=255, blank=True, null=True, verbose_name='awards')
    
    # SPECIAL
    aspect_ratio = models.CharField(max_length=255, blank=True, null=True, verbose_name='aspect ratio')
    scale = models.CharField(max_length=255, blank=True, null=True, verbose_name='scale')
    additional_scale_information = models.CharField(max_length=255, blank=True, null=True, verbose_name='additional scale information')
    format_of_notated_music = models.CharField(max_length=255, blank=True, null=True, verbose_name='format of notated music')
    sound_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='sound content')
    performer_narrator_or_presenter = models.CharField(max_length=255, blank=True, null=True, verbose_name='performer narrator or presenter')
    medium_of_performance = models.CharField(max_length=255, blank=True, null=True, verbose_name='medium of performance')
    colour_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='colour content')
    colour_content_of_resource_for_visual_impairments = models.CharField(max_length=255, blank=True, null=True, verbose_name='colour content of resource for visual impairments')
    other_details = models.CharField(max_length=255, blank=True, null=True, verbose_name='other details')
    projection = models.CharField(max_length=255, blank=True, null=True, verbose_name='projection')

    # Ei formissa
    #scale_of_still_image_or_three_dimensional_form = models.CharField(max_length=255, blank=True, null=True, verbose_name='scale of still image or three dimensional form')
    #colour_of_three_dimensional_form = models.CharField(max_length=255, blank=True, null=True, verbose_name='colour of three dimensional form')
    #color_of_moving_image = models.CharField(max_length=255, blank=True, null=True, verbose_name='colour of moving image')
    #colour_of_still_image = models.CharField(max_length=255, blank=True, null=True, verbose_name='coulour of still image')
    #form_of_musical_notation = models.CharField(max_length=255, blank=True, null=True, verbose_name='form of musical notation')
    #form_of_notated_movement = models.CharField(max_length=255, blank=True, null=True, verbose_name='form of notated movement')
    
    # Relations
    work_expressed = models.ManyToManyField('Work', through='WorkExpressed', related_name='Expression__work_expressed')
    manifestation_of_expression = models.ManyToManyField('Manifestation', through='ManifestationOfExpression', related_name='Expression__manifestation_of_expression')
    contributor_person = models.ManyToManyField('Person', through='Contributor', related_name='Expression__contributor_person') 
    contributor_family = models.ManyToManyField('Family', through='Contributor', related_name='Expression__contributor_family') 
    contributor_corporate_body = models.ManyToManyField('CorporateBody', through='Contributor', related_name='Expression__contributor_corporate_body') 
    related_expression = models.ManyToManyField('Expression', through='RelatedExpression', related_name='Expression__related_expression')
    
    def __unicode__(self):
        return "%s" % (identifier)
        
class Manifestation(models.Model):
    # CORE
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='title')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='copyright date')
    carrier_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='carrier type')
    extent = models.CharField(max_length=255, blank=True, null=True, verbose_name='extent')
    num_of_serials = models.CharField(max_length=255, blank=True, null=True, verbose_name='numbering of serials')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier for the manifestation')
    statement_responsibility = models.CharField(max_length=255, blank=True, null=True, verbose_name='statement of responsibility')
    statement_series = models.CharField(max_length=255, blank=True, null=True, verbose_name='series statement')
    statement_edition = models.CharField(max_length=255, blank=True, null=True, verbose_name='edition statement')
    statement_publication = models.CharField(max_length=255, blank=True, null=True, verbose_name='publication statement')
    statement_manufacture = models.CharField(max_length=255, blank=True, null=True, verbose_name='manufacture statement')
    statement_distribution = models.CharField(max_length=255, blank=True, null=True, verbose_name='distribution statement')
    
    # ENHANCED
    mediatype = models.CharField(max_length=255, blank=True, null=True, verbose_name='media type')
    dimensions = models.CharField(max_length=255, blank=True, null=True, verbose_name='dimensions')
    resource_locator = models.CharField(max_length=255, blank=True, null=True, verbose_name='uniform resource locator')
    citation = models.CharField(max_length=255, blank=True, null=True, verbose_name='preferred citation')
    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='note')
    production_statement = models.CharField(max_length=255, blank=True, null=True, verbose_name='production statement')
    restrictions_on_access = models.CharField(max_length=255, blank=True, null=True, verbose_name='restrictions on access')
    restrictions_on_use = models.CharField(max_length=255, blank=True, null=True, verbose_name='restrictions on use')
    contact = models.CharField(max_length=255, blank=True, null=True, verbose_name='contact information')
    terms = models.CharField(max_length=255, blank=True, null=True, verbose_name='terms of availability')

    # SPECIAL
    mode = models.CharField(max_length=255, blank=True, null=True, verbose_name='mode')
    frequency = models.CharField(max_length=255, blank=True, null=True, verbose_name='frequency')
    format = models.CharField(max_length=255, blank=True, null=True, verbose_name='format')
    font_size = models.CharField(max_length=255, blank=True, null=True, verbose_name='font size')
    reduction_ratio = models.CharField(max_length=255, blank=True, null=True, verbose_name='reduction size')
    polarity = models.CharField(max_length=255, blank=True, null=True, verbose_name='polarity')
    mount = models.CharField(max_length=255, blank=True, null=True, verbose_name='mount')
    production_method = models.CharField(max_length=255, blank=True, null=True, verbose_name='production method')
    layout = models.CharField(max_length=255, blank=True, null=True, verbose_name='layout')
    base_material = models.CharField(max_length=255, blank=True, null=True, verbose_name='base material')
    applied_material = models.CharField(max_length=255, blank=True, null=True, verbose_name='applied material')
    projection_characteristic = models.CharField(max_length=255, blank=True, null=True, verbose_name='projection characteristic')
    generation = models.CharField(max_length=255, blank=True, null=True, verbose_name='generation')
    video_characteristic = models.CharField(max_length=255, blank=True, null=True, verbose_name='video characteristic')
    digitalfile_characteristic = models.CharField(max_length=255, blank=True, null=True, verbose_name='digitalfile characteristic')
    sound_characteristic = models.CharField(max_length=255, blank=True, null=True, verbose_name='sound characteristic')
    sound_content = models.CharField(max_length=255, blank=True, null=True, verbose_name='sound content')
    equipment = models.CharField(max_length=255, blank=True, null=True, verbose_name='equipment')
    
    # Relations
    work_manifested = models.ManyToManyField('Work', through='WorkManifested')
    exemplar_of_manifestation = models.ManyToManyField('Item', through='ExemplarOfManifestation', related_name='Manifestation__exemplar_of_manifestation')
    expression_of_manifestation = models.ManyToManyField('Expression', through='ExpressionOfManifestation', related_name='Manifestation__expression_of_manifestation')
    producer_of_unpublished_resource_person = models.ManyToManyField('Person', through='ProducerOfUnpublishedResource', related_name='Manifestation__producer_of_unpublished_resource_person')
    producer_of_unpublished_resource_family = models.ManyToManyField('Family', through='ProducerOfUnpublishedResource', related_name='Manifestation__producer_of_unpublished_resource_family')
    producer_of_unpublished_resource_corporate_body  = models.ManyToManyField('CorporateBody', through='ProducerOfUnpublishedResource', related_name='Manifestation__producer_of_unpublished_resource_corporate_body')
    publisher_person = models.ManyToManyField('Person', through='Publisher', related_name='Manifestation__Producer_person')
    publisher_family = models.ManyToManyField('Family', through='Publisher', related_name='Manifestation__Producer_family')
    publisher_corporate_body = models.ManyToManyField('CorporateBody', through='Publisher', related_name='Manifestation__Producer_corporate_body')
    manufacturer_person = models.ManyToManyField('Person', through='Manufacturer', related_name='Manifestation__manufacturer_person')
    manufacturer_family = models.ManyToManyField('Family', through='Manufacturer', related_name='Manifestation__manufacturer_family')
    manufacturer_corporate_body = models.ManyToManyField('CorporateBody', through='Manufacturer', related_name='Manifestation__manufacturer_corporate_body')
    distributor_person = models.ManyToManyField('Person', through='Distributor', related_name='Manifestation__distributor_person')
    distributor_family = models.ManyToManyField('Family', through='Distributor', related_name='Manifestation__distributor_family')
    distributor_corporate_body = models.ManyToManyField('CorporateBody', through='Distributor', related_name='Manifestation__distributor_corporate_body')
    related_manifestation = models.ManyToManyField('Manifestation', through='RelatedManifestation', related_name='Manifestation__related_manifestation')

    # ACTOR
    other_person_associated_with_a_manifestation = models.ManyToManyField('Person', through='OtherActorAssociatedWithAManifestation', related_name='Manifestation__other_person_associated_with_a_manifestation')
    other_family_associated_with_a_manifestation = models.ManyToManyField('Family', through='OtherActorAssociatedWithAManifestation', related_name='Manifestation__other_family_associated_with_a_manifestation')
    other_corporate_body_associated_with_a_manifestation = models.ManyToManyField('CorporateBody', through='OtherActorAssociatedWithAManifestation', related_name='Manifestation__other_corporate_body_associated_with_a_manifestation')
    
    def __unicode__(self):
        return self.title
        
class Item(models.Model):
    # CORE
    
    # ENHANCED
    extent = models.CharField(max_length=255, blank=True, null=True, verbose_name='extent')
    contact = models.CharField(max_length=255, blank=True, null=True, verbose_name='contact information')
    citation = models.CharField(max_length=255, blank=True, null=True, verbose_name='preferred citation')
    resource_locator = models.CharField(max_length=255, blank=True, null=True, verbose_name='uniform resource locator')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier for the item')
    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='note')
    restrictions_on_access = models.CharField(max_length=255, blank=True, null=True, verbose_name='restrictions on access')
    restrictions_on_use = models.CharField(max_length=255, blank=True, null=True, verbose_name='restrictions on use')
    dimensions = models.CharField(max_length=255, blank=True, null=True, verbose_name='dimensions')
    
    # SPECIAL
    history = models.CharField(max_length=255, blank=True, null=True, verbose_name='history')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source')
    characteristics = models.CharField(max_length=255, blank=True, null=True, verbose_name='characteristics')
    
    # Relations
    manifestation_exemplified = models.ManyToManyField('Manifestation', through='ManifestationExemplified', related_name='Item__manifestation_exemplified')
    owner_person = models.ManyToManyField('Person', through='Owner', related_name='Item__owner_person')
    owner_family = models.ManyToManyField('Family', through='Owner', related_name='Item__owner_family')
    owner_corporate_body = models.ManyToManyField('CorporateBody', through='Owner', related_name='Item__owner_corporate_body')
    custodian_person = models.ManyToManyField('Person', through='Custodian', related_name='Item__custodian_person')
    custodian_family = models.ManyToManyField('Family', through='Custodian', related_name='Item__custodian_family')
    custodian_corporate_body = models.ManyToManyField('CorporateBody', through='Custodian', related_name='Item__custodian_corporate_body')
    other_person_associated_with_an_item = models.ManyToManyField('Person', through='OtherActorAssociatedWithAnItem', related_name='Item__other_person_associated_with_an_item')
    other_family_associated_with_an_item = models.ManyToManyField('Family', through='OtherActorAssociatedWithAnItem', related_name='Item__other_family_associated_with_an_item')
    other_corporate_body_associated_with_an_item = models.ManyToManyField('CorporateBody', through='OtherActorAssociatedWithAnItem', related_name='Item__other_corporate_body_associated_with_an_item')
    related_item = models.ManyToManyField('Item', through='RelatedItem', related_name='Item__related_item')
    
    def __unicode__(self):
        return "%s" % (self.identifier)
       
class Person(models.Model):
    # CORE
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='name of the person')
    fullername = models.CharField(max_length=255, blank=True, null=True, verbose_name='fuller form of name')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='date associated with the person')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='title of the person')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier for the person')
    activity = models.CharField(max_length=255, blank=True, null=True, verbose_name='field of activity of the person')
    profession = models.CharField(max_length=255, blank=True, null=True, verbose_name='profession or occupation')
    other = models.CharField(max_length=255, blank=True, null=True, verbose_name='other designation associated with the person')
    
    # ENHANCED
    biographical_information = models.CharField(max_length=255, blank=True, null=True, verbose_name='biographical information')
    affiliation = models.CharField(max_length=255, blank=True, null=True, verbose_name='affiliation')
    place_of_birth = models.CharField(max_length=255, blank=True, null=True, verbose_name='place of birth')
    place_of_death = models.CharField(max_length=255, blank=True, null=True, verbose_name='place of death')
    place_of_residence = models.CharField(max_length=255, blank=True, null=True, verbose_name='place of residence')
    country_associated = models.CharField(max_length=255, blank=True, null=True, verbose_name='country associated with the person')
    undifferentiated_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='undifferentiated name indicator')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='address of the person')
    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='note')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status_of_identification = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    gender = models.CharField(max_length=255, blank=True, null=True, verbose_name='gender')
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name='language of the person')
    
    # SPECIAL
    
    # Relations
    person_related_person = models.ManyToManyField('Person', through='PersonRelatedPerson', related_name='Person__person_related_person')
    person_related_family = models.ManyToManyField('Family', through='PersonRelatedFamily', related_name='Person__person_related_family')
    person_related_corporate_body = models.ManyToManyField('CorporateBody', through='PersonRelatedCorporateBody', related_name='Person__person_related_corporate_body')
        
    def __unicode__(self):
        return self.name
        
class Family(models.Model):
    # CORE
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='name of the family')
    type = models.CharField(max_length=255, blank=True, null=True, verbose_name='type of family')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='date associated with the family')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier for the family')
    member = models.CharField(max_length=255, blank=True, null=True, verbose_name='prominent member of the family')
    
    # ENHANCED
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='hereditary title')
    history = models.CharField(max_length=255, blank=True, null=True, verbose_name='family history')
    undifferentiated_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='undifferentiated name')
    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='note')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='stauts of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
    
    # Ei formissa
    #place = models.CharField(max_length=255, blank=True, null=True, verbose_name='place associated with the family')
    
    # Relations
    family_related_person = models.ManyToManyField('Person', through='FamilyRelatedPerson', related_name='Family__family_related_person')
    family_related_family = models.ManyToManyField('Family', through='FamilyRelatedFamily', related_name='Family__family_related_family')
    family_related_corporate_body = models.ManyToManyField('CorporateBody', through='FamilyRelatedCorporateBody', related_name='Family__family_related_corporate_body')
    
    def __unicode__(self):
        return self.name
        
class CorporateBody(models.Model):
    # CORE
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='name of the corporate body')
    associated = models.CharField(max_length=255, blank=True, null=True, verbose_name='associated institution')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='date associated with the corporate body')
    other = models.CharField(max_length=255, blank=True, null=True, verbose_name='other designation associated with the corporate body')
    place = models.CharField(max_length=255, blank=True, null=True, verbose_name='place associated with the corporate body')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier for the corporate body')
    
    # ENHANCED
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name='language of the corporate body')
    history = models.CharField(max_length=255, blank=True, null=True, verbose_name='corporate history')
    activity = models.CharField(max_length=255, blank=True, null=True, verbose_name='field of activity of the corporate body')
    num_of_conference = models.CharField(max_length=255, blank=True, null=True, verbose_name='number of a conference etc.')
    undifferentiated_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='undifferentiated name indicator')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='address of the corporate body')
    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='note')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
    
    # Relations
    corporate_body_related_person = models.ManyToManyField('Person', through='CorporateBodyRelatedPerson', related_name='CorporateBody__corporate_body_related_person')
    corporate_body_related_family = models.ManyToManyField('Family', through='CorporateBodyRelatedFamily', related_name='CorporateBody__corporate_body_related_family')
    corporate_body_related_corporate_body = models.ManyToManyField('CorporateBody', through='CorporateBodyRelatedCorporateBody', related_name='CorporateBody__corporate_body_related_corporate_body')
    
    def __unicode__(self):
        return self.name
        
class Concept(models.Model):
    # CORE
    
    # ENHANCED
    term = models.CharField(max_length=255, blank=True, null=True, verbose_name='term of concept')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier for the concept')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
    
    # Relations
    concept_related_concept = models.ManyToManyField('Concept', through='ConceptRelatedConcept', related_name='Concept__concept_related_concept')
    concept_related_event = models.ManyToManyField('Event', through='ConceptRelatedEvent', related_name='Concept__concept_related_event')
    concept_related_place = models.ManyToManyField('Place', through='ConceptRelatedPlace', related_name='Concept__concept_related_place')
    concept_related_object = models.ManyToManyField('Object', through='ConceptRelatedObject', related_name='Concept__concept_related_object')
    
    def __unicode__(self):
        return "%s" % (self.identifier)

class Object(models.Model):
    # CORE

    # ENHANCED
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='name of the object')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier of the object')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
    
    # Relations
    object_related_concept = models.ManyToManyField(Concept, through='ObjectRelatedConcept', related_name='Object__object_related_concept')
    object_related_event = models.ManyToManyField('Event', through='ObjectRelatedEvent', related_name='Object__object_related_event')
    object_related_place = models.ManyToManyField('Place', through='ObjectRelatedPlace', related_name='Object__object_related_place')
    object_related_object = models.ManyToManyField('Object', through='ObjectRelatedObject', related_name='Object__object_related_object')
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    # CORE
    
    # ENHANCED
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='name of the event')
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier of the event')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
    
    # Relations
    event_related_concept = models.ManyToManyField(Concept, through='EventRelatedConcept', related_name='Event__event_related_object')
    event_related_event = models.ManyToManyField('Event', through='EventRelatedEvent', related_name='Event__event_related_event')
    event_related_place = models.ManyToManyField('Place', through='EventRelatedPlace', related_name='Event__event_related_place')
    event_related_object = models.ManyToManyField(Object, through='EventRelatedObject', related_name='Event__event_related_object')
    
    def __unicode__(self):
        return self.name

class Place(models.Model):
    # CORE
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='name of the place')
    
    # ENHANCED
    identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name='identifier of the place')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
    
    # Relations
    place_related_concept = models.ManyToManyField(Concept, through='PlaceRelatedConcept', related_name='Place__place_related_concept')
    place_related_event = models.ManyToManyField(Event, through='PlaceRelatedEvent', related_name='Place__place_related_event')
    place_related_place = models.ManyToManyField('Place', through='PlaceRelatedPlace', related_name='Place__place_related_place')
    place_related_object = models.ManyToManyField(Object, through='PlaceRelatedObject', related_name='Place__place_related_object')
    
    def __unicode__(self):
        return self.name
        
class Name(models.Model):
    # CORE

    # ENHANCED
    scope = models.CharField(max_length=255, blank=True, null=True, verbose_name='scope of usage')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='date of usage')
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name='source consulted')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='status of identification')
    cataloguers_note = models.CharField(max_length=255, blank=True, null=True, verbose_name='cataloguers note')
    
    # SPECIAL
        
    def __unicode__(self):
        return "%s" % (self.scope)
        
# Work relations
class ExpressionOfWork(models.Model):
    # Kaanteinen suhde: Work Expressed
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Expression of Work')
    work_domain = models.ForeignKey(Work, related_name='ExpressionOfWork__work_domain')
    expression_range = models.ForeignKey(Expression, related_name='ExpressionOfWork__expression_range')
    
    def __unicode__(self):
        return self.name
        
class ManifestationOfWork(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Manifestation of Work')
    work_domain = models.ForeignKey(Work, related_name='ManifestationOfWork__work_domain')
    manifestation_range = models.ForeignKey(Manifestation, related_name='ManifestationOfWork__manifestation_range')
        
    def __unicode__(self):
        return self.name
        
class Creator(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Creator')
    work_domain = models.ForeignKey(Work, related_name='Creator__work_domain', blank=True, null=True)
    person_range = models.ForeignKey(Person, related_name='Creator__person_range', blank=True, null=True)
    family_range = models.ForeignKey(Family, related_name='Creator__family_range', blank=True, null=True)
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Creator__corporate_body_range', blank=True, null=True)
    
    def __unicode__(self):
        return self.name

        
class RelatedWork(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Work')
    work_domain = models.ForeignKey(Work, related_name='RelatedWork__work_domain')
    work_range = models.ForeignKey(Work, related_name='RelatedWork__work_range')
    
    def __unicode__(self):
        return self.name

# ACTOR
class OtherActorAssociatedWithAWork(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Other Person, Family, or Corporate Body Associated with a Work')
    work_domain = models.ForeignKey(Work, related_name='OtherActorAssociatedWithAWork__work_domain', blank=True, null=True)
    person_range = models.ForeignKey(Person, related_name='OtherActorAssociatedWithAWork__person_range', blank=True, null=True)
    family_range = models.ForeignKey(Family, related_name='OtherActorAssociatedWithAWork__family_range', blank=True, null=True)
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='OtherActorAssociatedWithAWork__corporate_body_range', blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
# Expression relations
class WorkExpressed(models.Model):
    # Kaanteinen suhde: Expression Of Work
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Work expressed')
    expression_domain = models.ForeignKey(Expression, related_name='WorkExpressed__expression_domain')
    work_range = models.ForeignKey(Work, related_name='WorkExpressed__work_range')
    
    def __unicode__(self):
        return self.name
        
class ManifestationOfExpression(models.Model):
    # Kaanteinen suhde: Expression of Manifestation
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Manifestation of Expression')
    expression_domain = models.ForeignKey(Expression, related_name='ManifestationOfExpression__expression_domain')
    manifestation_range = models.ForeignKey(Manifestation, related_name='ManifestationOfExpression__manifestation_range')
    
    def __unicode__(self):
        return self.name
        
class Contributor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Contributor')
    expression_domain = models.ForeignKey(Expression, related_name='Contributor__expression_domain')
    person_range = models.ForeignKey(Person, related_name='Contributor__person_range')
    family_range = models.ForeignKey(Family, related_name='Contributor__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Contributor__corporate_body_range')
    
    def __unicode__(self):
        return self.name
        
class RelatedExpression(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Expression')
    expression_domain = models.ForeignKey(Expression, related_name='RelatedExpression__expression_domain')
    expression_range = models.ForeignKey(Expression, related_name='RelatedExpression__expression_range')
    
    def __unicode__(self):
        return self.name

# Manifestation relations
class WorkManifested(models.Model):
    # Kaanteinen suhde: Manifestation of Work
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Work manifested')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='WorkManifested__manifestation_domain')
    work_range = models.ForeignKey(Work, related_name='WorkManifested__work_range')
    
    def __unicode__(self):
        return self.name
        
class ExemplarOfManifestation(models.Model):
    # Kaanteinen suhde: Manifestation Examplified
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Examplar of Manifestation')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='ExemplarOfManifestation__manifestation_domain')
    item_range = models.ForeignKey(Item, related_name='ExemplarOfManifestation__item_range')

    def __unicode__(self):
        return self.name
        
class ExpressionOfManifestation(models.Model):    
    # Kaanteinen suhde: Manifestation Of Expression
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Expression Of Manifestation')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='ExpressionOfManifestation__manifestation_domain')
    expression_range = models.ForeignKey(Expression, related_name='ExpressionOfManifestation__expression_range')
    
    def __unicode__(self):
        return self.name

class ProducerOfUnpublishedResource(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Producer of Unpublished Resource')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='ProducerOfUnpublishedResource__manifestation_domain')
    person_range = models.ForeignKey(Person, related_name='ProducerOfUnpublishedResource__person_range')
    family_range = models.ForeignKey(Family, related_name='ProducerOfUnpublishedResource__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='ProducerOfUnpublishedResource__corporate_body_range')
    
    def __unicode__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Publisher')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='Publisher__manifestation_domain')
    person_range = models.ForeignKey(Person, related_name='Publisher__person_range')
    family_range = models.ForeignKey(Family, related_name='Publisher__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Publisher__corporate_body_range')
    
    def __unicode__(self):
        return self.name
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Manufacturer')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='Manufacturer__manifestation_domain')
    person_range = models.ForeignKey(Person, related_name='Manufacturer__person_range')
    family_range = models.ForeignKey(Family, related_name='Manufacturer__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Manufacturer__corporate_body_range')
    
    def __unicode__(self):
        return self.name
    
class RelatedManifestation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Manifestation')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='RelatedManifestation__manifestation_domain')
    manifestation_range = models.ForeignKey(Manifestation, related_name='RelatedManifestation__manifestation_range')
    
    def __unicode__(self):
        return self.name

# ACTOR
class OtherActorAssociatedWithAManifestation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Other Person Family or Corporate Body associated with a Manifestation')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='OtherActorAssociatedWithAManifestation__manifestation_domain')
    person_range = models.ForeignKey(Person, related_name='OtherActorAssociatedWithAManifestation__person_range')
    family_range = models.ForeignKey(Family, related_name='OtherActorAssociatedWithAManifestation__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='OtherActorAssociatedWithAManifestation__corporate_body_range')

class Distributor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Distributor')
    manifestation_domain = models.ForeignKey(Manifestation, related_name='Distributor__manifestation_domain')
    person_range = models.ForeignKey(Person, related_name='Distributor__person_range')
    family_range = models.ForeignKey(Family, related_name='Distributor__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Distributor__corporate_body_range')
    
    def __unicode__(self):
        return self.name
    
# Item relations
class ManifestationExemplified(models.Model):
    # Kaanteinen suhde: Exemplar of Manifestation
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Manifestation Examplified')
    item_domain = models.ForeignKey(Item, related_name='ManifestationExemplified__item_domain')
    manifestation_range = models.ForeignKey(Manifestation, related_name='ManifestationExemplified__manifestation_range')

    def __unicode__(self):
        return self.name
        
class Owner(models.Model):    
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Owner')
    item_domain = models.ForeignKey(Item, related_name='Owner__item_domain')
    person_range = models.ForeignKey(Person, related_name='Owner__person_range')
    family_range = models.ForeignKey(Family, related_name='Owner__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Owner__corporate_body_range')
    
    def __unicode__(self):
        return self.name
    
class Custodian(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Custodian')
    item_domain = models.ForeignKey(Item, related_name='Custodian__item_domain')
    person_range = models.ForeignKey(Person, related_name='Custodian__person_range')
    family_range = models.ForeignKey(Family, related_name='Custodian__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='Custodian__corporate_body_range')
    
    def __unicode__(self):
        return self.name

class OtherActorAssociatedWithAnItem(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Other Person, Family, or Corporate Body Associated with an Item')
    item_domain = models.ForeignKey(Item, related_name='OtherActorAssociatedWithAnItem__item_domain')
    person_range = models.ForeignKey(Person, related_name='OtherActorAssociatedWithAnItem__person_range')
    family_range = models.ForeignKey(Family, related_name='OtherActorAssociatedWithAnItem__family_range')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='OtherActorAssociatedWithAnItem__corporate_body_range')
    
    def __unicode__(self):
        return self.name
        
class RelatedItem(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Item')
    item_domain = models.ForeignKey(Item, related_name='RelatedItem__item_domain')
    item_range = models.ForeignKey(Item, related_name='RelatedItem__item_range')
    
    def __unicode__(self):
        return self.name
        
# Person relations
class PersonRelatedPerson(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Person')
    person_domain = models.ForeignKey(Person, related_name='PersonRelatedPerson__person_domain')
    person_range = models.ForeignKey(Person, related_name='PersonRelatedPerson__person_range')
    
    def __unicode__(self):
        return self.name

class PersonRelatedFamily(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Family')
    person_domain = models.ForeignKey(Person, related_name='PersonRelatedFamily__person_domain')
    family_range = models.ForeignKey(Family, related_name='PersonRelatedFamily__family_range')
    
    def __unicode__(self):
        return self.name
        
class PersonRelatedCorporateBody(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Corporate Body')
    person_domain = models.ForeignKey(Person, related_name='PersonRelatedCorporateBody__person_domain')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='PersonRelatedCorporateBody__corporate_body_range')
    
    def __unicode__(self):
        return self.name

# Family relations
class FamilyRelatedFamily(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Family')
    family_domain = models.ForeignKey(Family, related_name='FamilyRelatedFamily__family_domain')
    family_range = models.ForeignKey(Family, related_name='FamilyRelatedFamily__family_range')
    
    def __unicode__(self):
        return self.name

class FamilyRelatedPerson(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Person')
    family_domain = models.ForeignKey(Family, related_name='FamilyRelatedPerson__family_domain')
    person_range = models.ForeignKey(Person, related_name='FamilyRelatedPerson__person_range')
    
    def __unicode__(self):
        return self.name
        
class FamilyRelatedCorporateBody(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Corporate Body')
    family_domain = models.ForeignKey(Family, related_name='FamilyRelatedCorporateBody__family_domain')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='FamilyRelatedCorporateBody__corporate_body_range')
    
    def __unicode__(self):
        return self.name 
        
# Corporate Body relations
class CorporateBodyRelatedCorporateBody(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Corporate Body')
    corporate_body_domain = models.ForeignKey(CorporateBody, related_name='CorporateBodyRelatedCorporateBody__corporate_body_domain')
    corporate_body_range = models.ForeignKey(CorporateBody, related_name='CorporateBodyRelatedCorporateBody__corporate_body_range')
    
    def __unicode__(self):
        return self.name 
        
class CorporateBodyRelatedFamily(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Family')
    corporate_body_domain = models.ForeignKey(CorporateBody, related_name='CorporateBodyRelatedFamily__corporate_body_domain')
    family_range = models.ForeignKey(Family, related_name='CorporateBodyRelatedFamily__family_range')
    
    def __unicode__(self):
        return self.name

class CorporateBodyRelatedPerson(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Person')
    corporate_body_domain = models.ForeignKey(CorporateBody, related_name='CorporateBodyRelatedPerson__corporate_body_domain')
    person_range = models.ForeignKey(Person, related_name='CorporateBodyRelatedPerson__person_range')
    
    def __unicode__(self):
        return self.name
        
# Concept relations
class ConceptRelatedConcept(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Concept')
    concept_domain = models.ForeignKey(Concept, related_name='ConceptRelatedConcept__concept_domain')
    concept_range = models.ForeignKey(Concept, related_name='ConceptRelatedConcept__concept_range')
    
    def __unicode__(self):
        return self.name 
        
class ConceptRelatedPlace(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Place')
    concept_domain = models.ForeignKey(Concept, related_name='ConceptRelatedPlace__concept_domain')
    place_range = models.ForeignKey(Place, related_name='ConceptRelatedPlace__place_range')
    
    def __unicode__(self):
        return self.name 

class ConceptRelatedEvent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Event')
    concept_domain = models.ForeignKey(Concept)
    event_range = models.ForeignKey(Event)
    
    def __unicode__(self):
        return self.name 
        
class ConceptRelatedObject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Object')
    concept_domain = models.ForeignKey(Concept)
    object_range = models.ForeignKey(Object)
    
    def __unicode__(self):
        return self.name 

# Object relations
class ObjectRelatedObject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Object')
    object_domain = models.ForeignKey(Object, related_name='ObjectRelatedObject__object_domain')
    object_range = models.ForeignKey(Object, related_name='ObjectRelatedObject__object_range')
    
    def __unicode__(self):
        return self.name 
        
class ObjectRelatedPlace(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Place')
    object_domain = models.ForeignKey(Object)
    place_range = models.ForeignKey(Place)
    
    def __unicode__(self):
        return self.name 

class ObjectRelatedEvent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Event')
    object_domain = models.ForeignKey(Object)
    event_range = models.ForeignKey(Event)
    
    def __unicode__(self):
        return self.name 
        
class ObjectRelatedConcept(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Concept')
    object_domain = models.ForeignKey(Object)
    concept_range = models.ForeignKey(Concept)
    
    def __unicode__(self):
        return self.name 
        
# Event relations
class EventRelatedEvent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Event')
    event_domain = models.ForeignKey(Event, related_name='EventRelatedEvent__event_domain')
    event_range = models.ForeignKey(Event, related_name='EventRelatedEvent__event_range')
    
    def __unicode__(self):
        return self.name 

class EventRelatedObject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Object')
    event_domain = models.ForeignKey(Event)
    object_range = models.ForeignKey(Object)
    
    def __unicode__(self):
        return self.name 
        
class EventRelatedPlace(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Place')
    event_domain = models.ForeignKey(Event)
    place_range = models.ForeignKey(Place)
    
    def __unicode__(self):
        return self.name 
        
class EventRelatedConcept(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Concept')
    event_domain = models.ForeignKey(Event)
    concept_range = models.ForeignKey(Concept)
    
    def __unicode__(self):
        return "%s" % (name)
        
# Place relations
class PlaceRelatedPlace(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Place')
    place_domain = models.ForeignKey(Place, related_name='PlaceRelatedPlace__place_domain')
    place_range = models.ForeignKey(Place, related_name='PlaceRelatedPlace__place_range')
    
    def __unicode__(self):
        return self.name 

class PlaceRelatedEvent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Event')
    place_domain = models.ForeignKey(Place, related_name='PlaceRelatedEvent__place_domain')
    event_range = models.ForeignKey(Event, related_name='PlaceRelatedEvent__event_range')
    
    def __unicode__(self):
        return self.name 

class PlaceRelatedObject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Object')
    place_domain = models.ForeignKey(Place)
    object_range = models.ForeignKey(Object)
    
    def __unicode__(self):
        return self.name 
        
class PlaceRelatedConcept(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Related Concept')
    place_domain = models.ForeignKey(Place)
    concept_range = models.ForeignKey(Concept)
    
    def __unicode__(self):
        return self.name
