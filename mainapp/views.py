import docx2txt
import fitz  # PyMuPDF
from django.shortcuts import render
from .forms import ResumeForm

import docx2txt
import fitz  # PyMuPDF
from django.shortcuts import render
from .forms import ResumeForm

JOB_KEYWORDS = {
    'doctor': ['mbbs', 'md', 'clinical', 'diagnosis', 'treatment', 'medical practice', 'patient care', 'hospital', 'medicine', 'surgeon', 'rounds'],
    'nurse': ['nursing', 'icu', 'patient care', 'hospital', 'emergency', 'bsc nursing', 'gnm', 'medication', 'vital signs', 'monitoring'],
    'pharmacist': ['pharmacy', 'medicines', 'dispensing', 'drug interactions', 'prescription', 'inventory', 'pharmacology'],
    'dentist': ['dental', 'oral care', 'cavity', 'tooth extraction', 'dentures', 'root canal', 'braces', 'clinic'],
    'physiotherapist': ['physiotherapy', 'rehabilitation', 'mobility', 'manual therapy', 'exercise therapy', 'pain relief'],
    'lab technician': ['lab', 'samples', 'microscope', 'blood test', 'pathology', 'reporting', 'equipment'],
    'medical transcriptionist': ['transcription', 'dictation', 'medical reports', 'audio typing', 'terminology', 'confidentiality'],

    'lawyer': ['legal', 'court', 'case', 'advocate', 'litigation', 'contract', 'legal advice', 'client', 'pleading'],
    'judge': ['judicial', 'hearing', 'judgment', 'case law', 'court', 'bench', 'verdict'],
    'legal advisor': ['legal advice', 'consultation', 'compliance', 'law', 'corporate law'],
    'notary public': ['notary', 'authentication', 'certify', 'affidavit', 'oath', 'documents'],
    'legal clerk': ['filing', 'case records', 'court assistance', 'scheduling', 'legal documentation'],

    'software developer': ['python', 'java', 'c++', 'git', 'api', 'backend', 'oop', 'debugging', 'programming'],
    'web developer': ['html', 'css', 'javascript', 'react', 'django', 'frontend', 'backend', 'node.js'],
    'frontend developer': ['html', 'css', 'javascript', 'react', 'ui', 'responsive design'],
    'backend developer': ['python', 'node.js', 'api', 'database', 'authentication', 'server'],
    'full-stack developer': ['frontend', 'backend', 'react', 'django', 'full-stack', 'api', 'ui'],
    'data analyst': ['excel', 'sql', 'powerbi', 'data cleaning', 'visualization', 'insights', 'tableau'],
    'data scientist': ['python', 'machine learning', 'data modeling', 'pandas', 'scikit-learn', 'statistics'],
    'cybersecurity expert': ['network security', 'firewall', 'ethical hacking', 'pen testing', 'vulnerabilities', 'encryption'],
    'mobile app developer': ['android', 'ios', 'flutter', 'react native', 'play store', 'xcode', 'ui/ux'],

    'mechanical engineer': ['solidworks', 'cad', 'mechanical', 'thermodynamics', 'manufacturing', 'design'],
    'civil engineer': ['autocad', 'construction', 'structure', 'site', 'surveying', 'estimation'],
    'electrical engineer': ['circuit', 'power', 'load', 'voltage', 'panel', 'design', 'distribution'],
    'electronics engineer': ['pcb', 'microcontroller', 'signal', 'semiconductor', 'sensor', 'arduino'],
    'computer engineer': ['networking', 'programming', 'systems', 'hardware', 'os', 'security'],
    'automobile engineer': ['vehicle', 'engine', 'automobile', 'repair', 'maintenance', 'testing'],

    'technician': ['troubleshoot', 'repair', 'installation', 'equipment', 'tools', 'wiring'],
    'mechanic': ['engine', 'vehicle', 'maintenance', 'bike', 'automobile', 'repair'],
    'plumber': ['pipe', 'fittings', 'water', 'leak', 'valve', 'installation'],
    'welder': ['welding', 'arc', 'mild steel', 'mig', 'tig', 'metal'],
    'cnc operator': ['cnc', 'lathe', 'machine', 'cutting', 'programming', 'drill'],

    'chartered accountant': ['ca', 'audit', 'tax', 'finance', 'ledger', 'balance sheet', 'compliance'],
    'company secretary': ['cs', 'company law', 'meetings', 'statutory', 'roc', 'compliance'],
    'banker': ['banking', 'loan', 'credit', 'customer', 'branch', 'transactions'],
    'accountant': ['tally', 'gst', 'income tax', 'accounting', 'invoice', 'ledger'],
    'investment analyst': ['stocks', 'equity', 'portfolio', 'risk analysis', 'market', 'returns'],

    'chef': ['cooking', 'kitchen', 'menu', 'recipe', 'food safety', 'ingredients'],
    'hotel manager': ['hospitality', 'guest', 'room', 'front office', 'booking', 'management'],
    'waiter': ['service', 'table', 'order', 'hospitality', 'customer'],
    'bartender': ['cocktail', 'mixing', 'bar', 'beverage', 'alcohol'],
    'baker': ['baking', 'bread', 'cake', 'oven', 'pastry', 'dough'],

    'school teacher': ['teaching', 'syllabus', 'lesson plan', 'student', 'classroom', 'homework'],
    'college professor': ['lecture', 'university', 'research', 'syllabus', 'seminar', 'paper'],
    'tuition teacher': ['coaching', 'subjects', 'board exam', 'students', 'classes'],
    'trainer': ['training', 'coaching', 'skills', 'mentoring', 'curriculum'],

    'ias': ['upsc', 'civil services', 'governance', 'policy', 'administration', 'public'],
    'police officer': ['law enforcement', 'crime', 'investigation', 'patrol', 'firs'],
    'defense': ['army', 'navy', 'air force', 'defense', 'training', 'operations'],
    'railway employee': ['railway', 'operations', 'track', 'station', 'train'],
    'post office staff': ['postal', 'mail', 'sorting', 'delivery', 'parcel'],

    'construction worker': ['masonry', 'cement', 'scaffolding', 'labor', 'construction'],
    'site supervisor': ['construction', 'site', 'supervision', 'labour', 'material'],
    'architect': ['design', 'autocad', 'blueprint', 'architecture', 'plan'],
    'mason': ['brick', 'plaster', 'cement', 'construction', 'labour'],

    'graphic designer': ['photoshop', 'illustrator', 'design', 'poster', 'layout'],
    'fashion designer': ['garment', 'fashion', 'trend', 'design', 'stitching'],
    'photographer': ['camera', 'dslr', 'shoot', 'editing', 'portrait'],
    'interior designer': ['space planning', 'decor', 'interior', 'furniture', 'autocad'],
    'animator': ['animation', '2d', '3d', 'vfx', 'maya', 'after effects'],

    'sales executive': ['sales', 'target', 'lead', 'crm', 'product', 'customer'],
    'digital marketer': ['seo', 'sem', 'google ads', 'social media', 'analytics'],
    'seo specialist': ['seo', 'keyword', 'ranking', 'backlink', 'optimization'],
    'content writer': ['content', 'blog', 'article', 'writing', 'grammar'],
    'social media manager': ['facebook', 'instagram', 'campaign', 'engagement', 'posts']
}

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def ats_score(resume_text, job_role):
    keywords = JOB_KEYWORDS.get(job_role.lower(), [])
    print(f"Keywords for {job_role}: {keywords}")
    score = 0
    matched = []
    for keyword in keywords:
        if keyword.lower() in resume_text.lower():
            score += 1
            matched.append(keyword)
            print(f"Matched: {keyword}")
    total = len(keywords)
    if total == 0:
        return "No keywords found for selected role.", []
    percentage = (score / total) * 100
    return f"ATS Score: {score}/{total} ({percentage:.0f}%)", matched

def upload_resume(request):
    result = None
    matched_keywords = []
    selected_role = None
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        selected_role = request.POST.get('job_role')
        
        # Debugging: Check if form is valid and job_role is present
        print(f"Form valid: {form.is_valid()}")
        print(f"Selected Role: {selected_role}")
        
        if form.is_valid() and selected_role:
            resume = form.save()
            file_path = resume.file.path
            
            # Debugging: Ensure the file is correctly uploaded
            print(f"File path: {file_path}")
            
            try:
                if file_path.endswith('.docx'):
                    resume_text = extract_text_from_docx(file_path)
                elif file_path.endswith('.pdf'):
                    resume_text = extract_text_from_pdf(file_path)
                else:
                    resume_text = ""
                
                # Debugging: Check if resume text is extracted properly
                print(f"Extracted Text: {resume_text[:500]}")  # Print first 500 characters of text

                if resume_text:
                    result, matched_keywords = ats_score(resume_text, selected_role)
                else:
                    result = "No text extracted from the resume."
            except Exception as e:
                result = f"Error reading file: {str(e)}"
        else:
            result = "Form is not valid or job role is not selected."
    else:
        form = ResumeForm()

    return render(request, 'upload.html', {
        'form': form,
        'result': result,
        'matched': matched_keywords,
        'roles': JOB_KEYWORDS.keys(),
        'selected_role': selected_role
    })
