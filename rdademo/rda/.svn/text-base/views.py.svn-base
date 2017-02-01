from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from rdademo.rda import forms
from rdademo.rda import models

def kysely(request, query=None):
    # Test
    if not query:
        query = request.GET.get('query', '')
        
    context = 'abc'
    template = 'rda/class.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response
    
def relations(request, url_cls, query):
    if url_cls == 'work':
        from rdademo.rda.models import Work
        object = Work.objects.get(id=query)
        template = 'rda/work.html'
        class_name = 'Work' 
        page_name = 'Relations'
    
        response = render_to_response(template, { 'object' : object, 'class_name' : class_name, 'page_name' : page_name }, context_instance=RequestContext(request))
        return response
        
    if url_cls == 'expression':
        from rdademo.rda.models import Expression
        object = Work.objects.get(id=query)
        template = 'rda/expression.html'
        class_name = 'Expression' 
        page_name = 'Relations'
    
        response = render_to_response(template, { 'object' : object, 'class_name' : class_name, 'page_name' : page_name }, context_instance=RequestContext(request))
        return response
        
def instances(request, url_cls):
    if url_cls == 'work':
        from rdademo.rda.models import Work
        object = Work.objects.all()
        template = 'rda/work.html'
        class_name = 'Work'
        page_name = 'Instances'
        
        response = render_to_response(template, { 'object' : object, 'class_name' : class_name, 'page_name' : page_name }, context_instance=RequestContext(request))
        return response
        
    if url_cls == 'expression':
        from rdademo.rda.models import Expression
        object = Expression.objects.all()
        template = 'rda/expression.html'
        class_name = 'Expression'
        page_name = 'Instances'
        
        response = render_to_response(template, { 'object' : object, 'class_name' : class_name, 'page_name' : page_name }, context_instance=RequestContext(request))
        return response
   
def index(request, url_cls):
    context = {'abc':url_cls}
    template = 'rda/class.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

def add(request, url_cls):
    
    #return HttpResponse(request.POST['title'])
    c = {}
    c.update(csrf(request))
    
    if request.method == 'POST':         
                          
        if url_cls == 'work':
            from rdademo.rda.models import Work
            work = Work()
            work_form = forms.WorkForm(request.POST)

            if work_form.is_valid():

                # Core
                work.title = work_form.cleaned_data['title']
                #work.preferred_title = work_form.cleaned_data['preferred_title']
                #work.variant_title = work_form.cleaned_data['variant_title']
                work.date = work_form.cleaned_data['date']
                work.origin = work_form.cleaned_data['origin']
                work.form = work_form.cleaned_data['form']
                work.other = work_form.cleaned_data['other']
                work.identifier = work_form.cleaned_data['identifier']
                #work.medium = work_form.cleaned_data['medium']
                work.signatory = work_form.cleaned_data['signatory']
                work.key = work_form.cleaned_data['key']
                work.designation = work_form.cleaned_data['designation']

                # Enhanced
                work.nature = work_form.cleaned_data['nature']
                work.coverage = work_form.cleaned_data['coverage']
                work.organization = work_form.cleaned_data['organization']
                work.audience = work_form.cleaned_data['audience']
                work.history = work_form.cleaned_data['history']
                work.epoch = work_form.cleaned_data['epoch']
                work.source = work_form.cleaned_data['source']
                work.status = work_form.cleaned_data['status']
                work.cataloguers_note = work_form.cleaned_data['cataloguers_note']
                work.status_of_id = work_form.cleaned_data['status_of_id']
                
                # Special
                work.academic_degree = work_form.cleaned_data['academic_degree']
                work.granting_institution = work_form.cleaned_data['granting_institution']
                work.year_granted = work_form.cleaned_data['year_granted']
                work.longitude = work_form.cleaned_data['longitude']
                work.latitude = work_form.cleaned_data['latitude']
                work.coord_pairs = work_form.cleaned_data['coord_pairs']
                work.right_asc_decl = work_form.cleaned_data['right_asc_decl']
                work.equinox = work_form.cleaned_data['equinox']
                
                work.save()
                            
            return HttpResponseRedirect('/rdademo/rda/work/attributes/add/')             
                
        if url_cls == 'expression':
                from rdademo.rda.models import Expression
                expression = Expression()
                expression_form = forms.ExpressionForm(request.POST)
                
                if expression_form.is_valid():
                    
                    # Core
                    expression.date = expression_form.cleaned_data['date']
                    expression.language_expression = expression_form.cleaned_data['language_expression']
                    expression.other = expression_form.cleaned_data['other']
                    expression.identifier = expression_form.cleaned_data['identifier']
                    expression.content_type = expression_form.cleaned_data['content_type']
 
                    # Enhanced
                    expression.credit = expression_form.cleaned_data['credit']
                    expression.duration = expression_form.cleaned_data['duration']
                    expression.language_content = expression_form.cleaned_data['language_content']
                    expression.place_and_date_of_capture = expression_form.cleaned_data['place_and_date_of_capture']
                    expression.accessibility_content = expression_form.cleaned_data['accessibility_content']
                    expression.illustrative_content = expression_form.cleaned_data['illustrative_content']
                    expression.form_of_notation = expression_form.cleaned_data['form_of_notation']
                    expression.script = expression_form.cleaned_data['script']
                    expression.form_of_tactile_notation = expression_form.cleaned_data['form_of_tactile_notation']
                    expression.summarization = expression_form.cleaned_data['summarization']
                    expression.supplementary_content = expression_form.cleaned_data['supplementary_content']
                    expression.source_consulted = expression_form.cleaned_data['source_consulted']
                    expression.status_of_identification = expression_form.cleaned_data['status_of_identification']
                    expression.cataloguers_note = expression_form.cleaned_data['cataloguers_note']
                    expression.awards = expression_form.cleaned_data['awards']
                    
                    # Special
                    expression.aspect_ratio = expression_form.cleaned_data['aspect_ratio']
                    expression.scale = expression_form.cleaned_data['scale']
                    expression.additional_scale_information = expression_form.cleaned_data['additional_scale_information']
                    expression.format_of_notated_music = expression_form.cleaned_data['format_of_notated_music']
                    expression.sound_content = expression_form.cleaned_data['sound_content']
                    expression.performer_narrator_or_presenter = expression_form.cleaned_data['performer_narrator_or_presenter'] 
                    expression.medium_of_performance = expression_form.cleaned_data['medium_of_performance']
                    expression.colour_content = expression_form.cleaned_data['colour_content']
                    expression.colour_content_of_resource_for_visual_impairments = expression_form.cleaned_data['colour_content_of_resource_for_visual_impairments']
                    expression.other_details = expression_form.cleaned_data['other_details']
                    expression.projection = expression_form.cleaned_data['projection']

                    # Ei formissa
                    #expression.scale_of_still_image_or_three_dimensional_form = form.cleaned_data['scale_of_still_image_or_three_dimensional_form']
                    #expression.colour_of_three_dimensional_form = form.cleaned_data['colour_of_three_dimensional_form']
                    #expression.color_of_moving_image = form.cleaned_data['colour_of_moving_image']
                    #expression.colour_of_still_image = form.cleaned_data['colour_of_still_image']
                    #expression.form_of_musical_notation = form.cleaned_data['musical_notation']
                    #expression.form_of_notated_movement = form.cleaned_data['notated_movement']
                    
                    expression.save()

                return HttpResponseRedirect('/rdademo/rda/expression/attributes/add/')

        if url_cls == 'manifestation':
                from rdademo.rda.models import Manifestation
                manifestation = Manifestation()
                manifestation_form = forms.ManifestationForm(request.POST)
                
                if manifestation_form.is_valid():
                
                    # CoreManifestationForm
                    manifestation.title = manifestation_form.cleaned_data['title']
                    manifestation.date = manifestation_form.cleaned_data['date'] 
                    manifestation.carrier_type = manifestation_form.cleaned_data['carrier_type'] 
                    manifestation.extent = manifestation_form.cleaned_data['extent'] 
                    manifestation.num_of_serials = manifestation_form.cleaned_data['num_of_serials'] 
                    manifestation.identifier = manifestation_form.cleaned_data['identifier']
                    manifestation.statement_responsibility = manifestation_form.cleaned_data['statement_responsibility']
                    manifestation.statement_series = manifestation_form.cleaned_data['statement_series'] 
                    manifestation.statement_edition = manifestation_form.cleaned_data['statement_edition'] 
                    manifestation.statement_publication = manifestation_form.cleaned_data['statement_publication']
                    manifestation.statement_manufacture = manifestation_form.cleaned_data['statement_manufacture']
                    manifestation.statement_distribution = manifestation_form.cleaned_data['statement_distribution'] 
                    
                    # EnhancedManifestationForm
                    manifestation.mediatype = manifestation_form.cleaned_data['mediatype']
                    manifestation.dimensions = manifestation_form.cleaned_data['dimensions']
                    manifestation.resource_locator = manifestation_form.cleaned_data['resource_locator'] 
                    manifestation.citation = manifestation_form.cleaned_data['citation'] 
                    manifestation.note = manifestation_form.cleaned_data['note'] 
                    manifestation.production_statement = manifestation_form.cleaned_data['production_statement']
                    manifestation.restrictions_on_access = manifestation_form.cleaned_data['restrictions_on_access'] 
                    manifestation.restrictions_on_use = manifestation_form.cleaned_data['restrictions_on_use'] 
                    manifestation.contact = manifestation_form.cleaned_data['contact'] 
                    manifestation.terms = manifestation_form.cleaned_data['terms'] 
                    
                    # SpecialManifestationForm
                    manifestation.mode = manifestation_form.cleaned_data['mode'] 
                    manifestation.frequency = manifestation_form.cleaned_data['frequency'] 
                    manifestation.format = manifestation_form.cleaned_data['format'] 
                    manifestation.font_size = manifestation_form.cleaned_data['font_size'] 
                    manifestation.reduction_ratio = manifestation_form.cleaned_data['reduction_ratio'] 
                    manifestation.polarity = manifestation_form.cleaned_data['polarity'] 
                    manifestation.mount = manifestation_form.cleaned_data['mount'] 
                    manifestation.production_method = manifestation_form.cleaned_data['production_method'] 
                    manifestation.layout = manifestation_form.cleaned_data['layout'] 
                    manifestation.base_material = manifestation_form.cleaned_data['base_material'] 
                    manifestation.applied_material = manifestation_form.cleaned_data['applied_material'] 
                    manifestation.projection_characteristic = manifestation_form.cleaned_data['projection_characteristic'] 
                    manifestation.generation = manifestation_form.cleaned_data['generation'] 
                    manifestation.video_characteristic = manifestation_form.cleaned_data['video_characteristic'] 
                    manifestation.digitalfile_characteristic = manifestation_form.cleaned_data['digitalfile_characteristic'] 
                    manifestation.sound_characteristic = manifestation_form.cleaned_data['sound_characteristic'] 
                    manifestation.sound_content = manifestation_form.cleaned_data['sound_content'] 
                    manifestation.equipment = manifestation_form.cleaned_data['equipment'] 
                   
                    manifestation.save()
                    
                return HttpResponseRedirect('/rdademo/rda/manifestation/attributes/add/')
                
        if url_cls == 'item':
                from rdademo.rda.models import Item
                item = Item()
                item_form = forms.ItemForm(request.POST)
                
                if item_form.is_valid():
                
                    # CoreItemForm
                    
                    # EnhancedItemForm
                    item.extent = item_form.cleaned_data['extent']  
                    item.contact = item_form.cleaned_data['contact'] 
                    item.citation = item_form.cleaned_data['citation']  
                    item.resource_locator = item_form.cleaned_data['resource_locator'] 
                    item.identifier = item_form.cleaned_data['identifier'] 
                    item.note = item_form.cleaned_data['note'] 
                    item.restrictions_on_access = item_form.cleaned_data['restrictions_on_access'] 
                    item.restrictions_on_use = item_form.cleaned_data['restrictions_on_use']  
                    item.dimensions = item_form.cleaned_data['dimensions']  
                    
                    # SpecialItemForm
                    item.history = item_form.cleaned_data['history']  
                    item.source = item_form.cleaned_data['source']  
                    item.characteristics = item_form.cleaned_data['characteristics']  
                    item.save()
                    
                return HttpResponseRedirect('/rdademo/rda/item/attributes/add/')
                
        if url_cls == 'person':
                from rdademo.rda.models import Person
                person = Person()
                person_form = forms.PersonForm(request.POST)
                
                if person_form.is_valid():
                
                    # CorePersonForm
                    person.name = person_form.cleaned_data['name']   
                    person.fullername = person_form.cleaned_data['fullername']   
                    person.date = person_form.cleaned_data['date']   
                    person.title = person_form.cleaned_data['title']   
                    person.identifier = person_form.cleaned_data['identifier']  
                    person.activity = person_form.cleaned_data['activity']   
                    person.profession = person_form.cleaned_data['profession']   
                    person.other = person_form.cleaned_data['other']   
                    
                    # EnhancedPersonForm
                    person.biographical_information = person_form.cleaned_data['biographical_information']   
                    person.affiliation = person_form.cleaned_data['affiliation']  
                    person.place_of_birth = person_form.cleaned_data['place_of_birth']  
                    person.place_of_death = person_form.cleaned_data['place_of_death']  
                    person.place_of_residence = person_form.cleaned_data['place_of_residence']   
                    person.country_associated = person_form.cleaned_data['country_associated']   
                    person.undifferentiated_name = person_form.cleaned_data['undifferentiated_name']   
                    person.address = person_form.cleaned_data['address']  
                    person.note = person_form.cleaned_data['note']   
                    person.source = person_form.cleaned_data['source']   
                    person.status_of_identification = person_form.cleaned_data['status_of_identification']  
                    person.cataloguers_note = person_form.cleaned_data['cataloguers_note']  
                    person.gender = person_form.cleaned_data['gender'] 
                    person.language = person_form.cleaned_data['language'] 
                    
                    # SpecialPersonForm
                    
                    person.save()
                    
                return HttpResponseRedirect('/rdademo/rda/person/attributes/add/')
                
        if url_cls == 'family':
                from rdademo.rda.models import Family
                family = Family()
                family_form = forms.FamilyForm(request.POST)
                
                if family_form.is_valid():
                
                    # CoreFamilyForm
                    family.name = family_form.cleaned_data['name'] 
                    family.type = family_form.cleaned_data['type'] 
                    family.date = family_form.cleaned_data['date'] 
                    family.identifier = family_form.cleaned_data['identifier'] 
                    family.member = family_form.cleaned_data['member'] 
                    
                    # EnhancedFamilyForm
                    family.title = family_form.cleaned_data['title'] 
                    family.history = family_form.cleaned_data['history'] 
                    family.undifferentiated_name = family_form.cleaned_data['undifferentiated_name'] 
                    family.note = family_form.cleaned_data['note'] 
                    family.source = family_form.cleaned_data['source'] 
                    family.status = family_form.cleaned_data['status'] 
                    family.cataloguers_note = family_form.cleaned_data['cataloguers_note'] 
                    
                    # SpecialFamilyForm
                    
                    # Ei formissa
                    # family.place = form.cleaned_data['place'] 
                    
                    family.save()
                    
                return HttpResponseRedirect('/rdademo/rda/family/attributes/add/')
                
        if url_cls == 'corporate_body':
                from rdademo.rda.models import CorporateBody
                corporate_body = CorporateBody()
                corporate_body_form = forms.CorporateBodyForm(request.POST)
                
                if corporate_body_form.is_valid():
                
                    # CoreCorporateBodyForm
                    corporate_body.name = corprate_body_form.cleaned_data['name']  
                    corporate_body.associated = corprate_body_form.cleaned_data['associated'] 
                    corporate_body.date = corprate_body_form.cleaned_data['date']  
                    corporate_body.other = corprate_body_form.cleaned_data['other']  
                    corporate_body.place = corprate_body_form.cleaned_data['place']  
                    corporate_body.identifier = corprate_body_form.cleaned_data['identifier']  
                    
                    # EnhancedCorporateBodyForm
                    corporate_body.language = corprate_body_form.cleaned_data['language'] 
                    corporate_body.history = corprate_body_form.cleaned_data['history'] 
                    corporate_body.activity = corprate_body_form.cleaned_data['activity'] 
                    corporate_body.num_of_conference = corprate_body_form.cleaned_data['num_of_conference']  
                    corporate_body.undifferentiated_name = corprate_body_form.cleaned_data['undifferentiated_name'] 
                    corporate_body.address = corprate_body_form.cleaned_data['address'] 
                    corporate_body.note = corprate_body_form.cleaned_data['note'] 
                    corporate_body.source = corprate_body_form.cleaned_data['source']  
                    corporate_body.status = corprate_body_form.cleaned_data['status']  
                    corporate_body.cataloguers_note = corprate_body_form.cleaned_data['cataloguers_note']  
                    
                    # SpecialCorporateBodyForm
                    
                    corporate_body.save()
                    
                return HttpResponseRedirect('/rdademo/rda/corprate_body/attributes/add/')
                
        if url_cls == 'concept':
                from rdademo.rda.models import Concept
                concept = Concept()
                concept_form = forms.ConceptForm(request.POST)
                
                if concept_form.is_valid():
                
                    # CoreConceptForm
                    
                    # EnhancedConceptForm
                    concept.term = concept_form.cleaned_data['term']  
                    concept.identifier = concept_form.cleaned_data['identifier']  
                    concept.source = concept_form.cleaned_data['source']   
                    concept.status = concept_form.cleaned_data['status']   
                    concept.cataloguers_note = concept_form.cleaned_data['cataloguers_note']   
                    
                    # SpecialConceptForm
                    
                    concept.save()
                    
                return HttpResponseRedirect('/rdademo/rda/concept/attributes/add/')
                
        if url_cls == 'object':
                from rdademo.rda.models import Object
                object = Object()
                object_form = forms.ObjectForm(request.POST)
                
                if object_form.is_valid():
                    
                    # CoreObjectForm
                    
                    # EnhancedObjectForm
                    object.name = object_form.cleaned_data['name']  
                    object.identifier = object_form.cleaned_data['identifier']  
                    object.source = object_form.cleaned_data['source']   
                    object.status = object_form.cleaned_data['status']   
                    object.cataloguers_note = object_form.cleaned_data['cataloguers_note']   
                    
                    # SpecialObjectForm
                    
                    object.save()
                    
                return HttpResponseRedirect('/rdademo/rda/object/attributes/add/')
                
        if url_cls == 'event':
                from rdademo.rda.models import Event
                event = Event()
                event_form = forms.EventForm(request.POST)
                
                if event_form.is_valid():
                
                    # CoreEventForm
                    
                    # EnhancedEventForm
                    event.name = event_form.cleaned_data['name']  
                    event.identifier = event_form.cleaned_data['identifier']  
                    event.source = event_form.cleaned_data['source']   
                    event.status = event_form.cleaned_data['status']   
                    event.cataloguers_note = event_form.cleaned_data['cataloguers_note']   
                    
                    # SpecialEventForm
                    
                    event.save()
                    
                return HttpResponseRedirect('/rdademo/rda/event/attributes/add/')
                                
        if url_cls == 'place':
                from rdademo.rda.models import Place
                place = Place()
                place_form = forms.PlaceForm(request.POST)
                
                if place_form.is_valid():
                
                    # Core
                    place.name = place_form.cleaned_data['name']  
                    
                    # Enhanced
                    place.identifier = place_form.cleaned_data['identifier']  
                    place.source = place_form.cleaned_data['source']   
                    place.status = place_form.cleaned_data['status']   
                    place.cataloguers_note = place_form.cleaned_data['cataloguers_note']   
                    
                    # Special
                    
                    place.save()
                    
                return HttpResponseRedirect('/rdademo/rda/place/attributes/add/')
                          
        if url_cls == 'name':
                from rdademo.rda.models import Name
                name = Name()
                name_form = forms.NameForm(request.POST)
                
                if name_form.is_valid():
                    
                    # CoreNameForm
                    
                    # EnhancedNameForm
                    name.scope = name_form.cleaned_data['scope']  
                    name.date = name_form.cleaned_data['date'] 
                    name.source = name_form.cleaned_data['source']   
                    name.status = name_form.cleaned_data['status']   
                    name.cataloguers_note = name_form.cleaned_data['cataloguers_note']   
                    
                    # SpecialNameForm
                    
                    name.save()
                          
                return HttpResponseRedirect('/rdademo/rda/name/attributes/add/')

    else:
        if url_cls == 'work':
            form = forms.WorkForm()
            class_name = 'Work'
            page_name = 'Attributes'
            template = 'rda/work.html'
        if url_cls == 'expression':
            form = forms.ExpressionForm()
            class_name = 'Expression'
            page_name = 'Attributes'
            template = 'rda/expression.html'
        if url_cls == 'manifestation':
            form = forms.ManifestationForm()
            class_name = 'Manifestation'
            page_name = 'Attributes'
            template = 'rda/manifestation.html'
        if url_cls == 'item':
            form = forms.ItemForm()
            class_name = 'Item'
            page_name = 'Attributes'
            template = 'rda/item.html'
        if url_cls == 'person':
            form = forms.PersonForm()
            class_name = 'Person'
            page_name = 'Attributes'
            template = 'rda/person.html'
        if url_cls == 'family':
            form = forms.FamilyForm()
            class_name = 'Family'
            page_name = 'Attributes'
            template = 'rda/family.html'
        if url_cls == 'corporate_body':
            form = forms.CorporateBodyForm()
            class_name = 'Corporate Body'
            page_name = 'Attributes'
            template = 'rda/corporate_body.html'
        if url_cls == 'concept':
            form = forms.ConceptForm()
            class_name = 'Concept'
            page_name = 'Attributes'
            template = 'rda/concept.html'
        if url_cls == 'object':
            form = forms.ObjectForm()
            class_name = 'Object'
            page_name = 'Attributes'
            template = 'rda/object.html'
        if url_cls == 'event':
            form = forms.EventForm()
            class_name = 'Event'
            page_name = 'Attributes'
            template = 'rda/event.html'
        if url_cls == 'place':
            form = forms.PlaceForm()
            class_name = 'Place'
            page_name = 'Attributes'
            template = 'rda/place.html'
        if url_cls == 'name':        
            form = forms.NameForm()
            class_name = 'Name'
            page_name = 'Attributes'
            template = 'rda/name.html'
                   
        return render_to_response(template, {
            'form': form,
            'class_name': class_name,
            'page_name' : page_name,
            'c': c,
        },
        context_instance=RequestContext(request))
