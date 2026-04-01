# simple_chat_faq_bot.py

import re

def normalize(text: str) -> str:
    """Lowercase and remove extra spaces."""
    return re.sub(r"\s+", " ", text.strip().lower())

def print_welcome():
    print("=" * 70)
    print("   🤖 Cyber Helper Bot")
    print("=" * 70)
    print("Hello 😊 I'm your calm cybersecurity & registration assistant.")
    print("You can ask me things like:")
    print(" - how do i register")
    print(" - how can i apply for a course")
    print(" - what qualifications do i need")
    print(" - what documents are required")
    print(" - what is cybersecurity")
    print(" - do i need coding")
    print(" - is cybersecurity hard")
    print(" - is the course free / scholarships")
    print(" - how many hours per week")
    print(" - what jobs can i get")
    print(" - what are prerequisites")
    print(" - how are exams done")
    print(" - how to access labs")
    print(" - how are grades calculated")
    print(" - is there tutoring support")
    print(" - what about group projects")
    print(" - can i study part-time")
    print(" - what's the course syllabus")
    print(" - when does the course start")
    print(" - how do i contact support")
    print("Type 'help' to see this list again.")
    print("Type 'exit' or 'quit' to leave the chat.")
    print("-" * 70)

def get_response(user_input: str) -> str:
    text = normalize(user_input)

    # Exit handled outside, but keep here in case you want to reuse.
    if text in {"exit", "quit", "bye", "goodbye"}:
        return "Thank you for chatting with me. I wish you a smooth learning journey in cybersecurity. 🌱"

    # REGISTRATION & ADMIN
    if "register" in text or "enroll" in text:
        return (
            "Thank you for asking. To register, log in to the student portal, open the "
            "'Courses' or 'Registration' section, search for the cybersecurity unit, "
            "and click 'Enroll'. If you get stuck, kindly take a screenshot and contact "
            "the ICT or registrar's office so they can guide you step by step."
        )

    if "deadline" in text or "last day" in text:
        return (
            "Registration deadlines are set by the registrar each semester. Please check "
            "the latest academic calendar on the school website or student portal. If you "
            "are unsure, it is safer to confirm directly with the registrar's office."
        )

    if "fees" in text or "payment" in text or "school fees" in text:
        return (
            "For fee details, please refer to the official fee structure from the finance "
            "office or the school website. Cybersecurity units are usually part of your "
            "normal program fees, but extra certifications may have separate charges."
        )

    if "portal" in text and ("login" in text or "log in" in text):
        return (
            "If you cannot log in to the portal, first confirm your username and password, "
            "then try the 'Forgot password' option. If it still fails, kindly visit or "
            "email the ICT helpdesk so they can reset your account."
        )

    # COURSE STRUCTURE & STUDY LOAD
    if "hours" in text or "per week" in text or "workload" in text:
        return (
            "Most students should plan about 6–10 hours per week for cybersecurity: "
            "watching lessons, doing labs, and revising. You can treat it like a part‑time job: "
            "a bit each day is better than last‑minute cramming."
        )

    if "duration" in text or "how long" in text:
        return (
            "The main introductory cybersecurity course usually runs for one semester or "
            "a few months, depending on the program. Short trainings or bootcamps can last "
            "from a few days to a few weeks."
        )

    if "prerequisite" in text or "requirements" in text or "requirement" in text:
        return (
            "Most beginner cybersecurity courses do not have strict prerequisites, but it "
            "helps to be comfortable with basic computer use, the internet, and simple logic. "
            "For advanced units, you may need prior programming or networking knowledge."
        )

    if "exam" in text or "assessment" in text or "test" in text:
        return (
            "Assessments often include quizzes, practical labs, assignments, and final exams. "
            "Cybersecurity focuses a lot on hands‑on practice, so lab work is usually very important."
        )

    if "online" in text or "physical" in text or "mode" in text:
        return (
            "Cybersecurity can be offered online, physical, or blended. Please check your "
            "course outline or timetable to see the official mode for your class this semester."
        )

    # CYBERSECURITY BASICS
    if "what is cybersecurity" in text or ("cybersecurity" in text and "what" in text):
        return (
            "Cybersecurity is the practice of protecting computers, networks, and data from "
            "attacks, damage, or unauthorized access. You can think of it as digital locks, "
            "guards, and alarms that keep information safe."
        )

    if "why is cybersecurity important" in text or ("important" in text and "cyber" in text):
        return (
            "Cybersecurity is important because almost everything today is connected and stores "
            "sensitive data—money, health records, school systems, and more. Good security protects "
            "people and organizations from fraud, data leaks, and serious damage."
        )

    if "hard" in text and "cyber" in text:
        return (
            "Cybersecurity can feel challenging at first, but it becomes easier when you take it "
            "step by step. If you are curious, patient, and willing to practice, you will improve "
            "steadily. It is normal to feel lost in the beginning."
        )

    if "math" in text and "need" in text:
        return (
            "You do not need very advanced math to start cybersecurity. Basic arithmetic and logical "
            "thinking are enough at the beginner level. Later, some areas like cryptography can use "
            "more math, but you can grow into that slowly."
        )

    if ("coding" in text or "programming" in text) and "need" in text:
        return (
            "You do not need to be a coding expert to begin, but learning some programming helps a lot. "
            "Languages like Python are friendly for beginners. Start small—simple scripts—and over time "
            "you will be comfortable automating tasks and analyzing data."
        )

    if "skills" in text or "what skills" in text:
        return (
            "Useful skills for cybersecurity include: basic networking, Linux commands, scripting "
            "(for example in Python), problem‑solving, attention to detail, and good communication. "
            "Start with the basics and build one layer at a time."
        )

    # CAREER & PATH
    if "job" in text or "career" in text or "salary" in text:
        return (
            "Cybersecurity offers many careers: security analyst, penetration tester, SOC analyst, "
            "security engineer, incident responder, and more. Salaries depend on country, experience, "
            "and certifications, but the field is growing with strong demand."
        )

    if "certification" in text or "certificate" in text:
        return (
            "Popular beginner‑friendly certifications include CompTIA Security+, Certified Cybersecurity "
            "Technician (CCT), and various vendor‑specific certs. It is usually best to first build a "
            "good foundation, then choose a certification that matches your goals."
        )

    if "path" in text or "roadmap" in text:
        return (
            "A simple path is: learn computer and networking basics, then Linux, then introductory "
            "cybersecurity concepts, and finally specialize (like ethical hacking, blue‑team defense, "
            "or cloud security). Move at a pace that feels realistic for you."
        )

    # STUDY TIPS
    if "how to study" in text or "study tips" in text or "how do i pass" in text:
        return (
            "To study cybersecurity well, try this: create a weekly plan, watch or read theory, then "
            "immediately practice in labs or virtual machines. Take small notes, ask questions early, "
            "and review mistakes calmly instead of fearing them."
        )

    if "resources" in text or "learn more" in text:
        return (
            "You can learn more using your course materials, official documentation, and trusted online "
            "platforms. Look for beginner‑friendly courses, practice labs, and official vendor training. "
            "Always be careful with random hacking blogs that suggest illegal activities."
        )

    if "illegal" in text or "hack" in text or "hacking" in text:
        return (
            "Ethical hacking is about testing and improving security with clear permission. Illegal hacking "
            "without consent is a crime. Always practice only in legal environments such as your school labs, "
            "CTF platforms, or systems where you have written permission."
        )

    # LABS & TOOLS
    if "lab" in text or "labs" in text or "practical" in text:
        return (
            "Cybersecurity labs may be provided through a virtual lab platform, virtual machines, or local "
            "tools like Kali Linux. Please check your course guide or ask your instructor which lab "
            "environment your class is using this semester."
        )

    if "tool" in text or "tools" in text:
        return (
            "Common cybersecurity tools include network scanners, vulnerability scanners, password‑cracking "
            "tools, and log analyzers. Your course will usually introduce them gradually and explain how to "
            "use them responsibly."
        )

    # HELP, CONTACT, GENERAL
    if text == "help":
        return (
            "I can help with: registration, admission, application process, qualifications, required documents, "
            "course content, syllabus, deadlines, fees, scholarships, financial aid, working hours, grades, "
            "group projects, tutoring, cybersecurity basics, difficulty level, skills needed, job opportunities, "
            "certifications, career paths, labs, tools, study tips, part-time options, contact information, "
            "support services, and alumni networks. Just ask a question in simple English!"
        )

    if "hello" in text or "hi" in text or "hey" in text:
        return "Hello! 😊 How can I help you with cybersecurity or course registration today?"

    # APPLICATION & ADMISSION
    if ("apply" in text or "application" in text) and ("course" in text or "program" in text):
        return (
            "To apply for the cybersecurity course, visit the school website and look for the 'Admissions' "
            "or 'Apply Now' section. You will typically need to fill out an application form, provide your "
            "qualifications, and any required documents. If you need help with the process, contact the "
            "admissions office or registrar. The application deadline is usually published on the website."
        )

    if "qualifications" in text or "eligible" in text or "eligibility" in text:
        return (
            "Most cybersecurity courses have basic admission requirements. Typically, you need a secondary "
            "school certificate or equivalent, and sometimes a basic computer literacy test. Some programs "
            "may have additional requirements like a minimum GPA or entrance exam. Check your school's "
            "specific requirements on their website or contact admissions for details."
        )

    if "documents" in text or "required documents" in text or "documents needed" in text:
        return (
            "Common documents needed for admission usually include: birth certificate or ID, secondary school "
            "transcripts, proof of payment/fee receipt, and sometimes proof of residence. You may also need "
            "a recommendation letter or statement of purpose. Please check the admission checklist on your "
            "school website or contact the admissions office for the exact list."
        )

    if "start date" in text or "when does" in text or "course begin" in text:
        return (
            "Cybersecurity courses typically start at the beginning of each semester or academic term. "
            "Please check the academic calendar on your school website for the exact start date. If you "
            "have already applied, you can check your enrollment status on the student portal."
        )

    if "contact" in text or "support" in text or "help desk" in text:
        return (
            "For general inquiries, visit the school's main website for department contacts. For technical "
            "issues with the student portal or labs, contact the ICT helpdesk. For course-specific questions, "
            "reach out to the cybersecurity department or your course instructor. Most schools also have an "
            "admissions email and phone number on their website."
        )

    if "scholarship" in text or "financial aid" in text or "funding" in text:
        return (
            "For information about scholarships and financial aid, visit the finance or student services office "
            "on campus or check the school website. Many schools offer merit-based scholarships, need-based aid, "
            "and payment plans. Deadlines for scholarship applications are usually earlier than the course start date."
        )

    if "syllabus" in text or "course content" in text or "curriculum" in text:
        return (
            "You can usually find the course syllabus and content outline on the school website under the course "
            "catalog or your student portal after enrollment. The syllabus lists topics, learning outcomes, assessment "
            "methods, and reading materials. If you can't find it, ask your course instructor or the department."
        )

    if "assignment" in text or "project" in text or "coursework" in text:
        return (
            "Assignments and projects are typically submitted through the student portal or learning management system. "
            "Details including deadlines, submission format, and grading criteria are usually provided in the course syllabus "
            "and by your instructor. Make sure to submit on time to avoid penalties."
        )

    if "group work" in text or "collaboration" in text or "team project" in text:
        return (
            "Many cybersecurity courses include group projects to build teamwork skills. Your instructor will assign groups "
            "and provide guidelines for collaboration. Most schools use online platforms or meeting tools to help teams work together. "
            "Communicate clearly with your team and report issues to your instructor if needed."
        )

    if "grade" in text or "marks" in text or "scoring" in text or "how am i graded" in text:
        return (
            "Grading typically includes: class participation, assignments, practical labs and projects, quizzes, midterms, and final exams. "
            "The exact breakdown and scale are in your course syllabus. You can usually check your grades on the student portal. "
            "If you have questions about a grade, contact your instructor respectfully."
        )

    if "credit" in text or "credit hours" in text or "units" in text:
        return (
            "The number of credit hours or units for the cybersecurity course is listed in the course catalog and on the student portal. "
            "Credit hours represent your workload and how the course contributes to your degree. Check your official course documentation "
            "or contact your academic advisor for details."
        )

    if "part time" in text or "part-time" in text or "flexible" in text or "schedule" in text:
        return (
            "Some cybersecurity programs offer part-time options or flexible schedules. Check the course description on the school website "
            "to see if this option is available. Part-time study may take longer to complete but allows you to balance work and study. "
            "Contact the program coordinator for more details about schedule flexibility."
        )

    if "tutor" in text or "tutoring" in text or "extra help" in text:
        return (
            "Most schools offer free tutoring through learning support centers. Many cybersecurity labs also include instructor office hours "
            "and peer study groups. Check your student portal or contact your instructor for available support options. Don't hesitate to ask "
            "for help—it shows you care about learning!"
        )

    if "appeal" in text or "complaint" in text or "grade dispute" in text:
        return (
            "If you have a concern about your grade or the course, first discuss it respectfully with your instructor. If unresolved, contact "
            "the department head or academic affairs office. Most schools have formal procedures for grade appeals. Document your concerns clearly "
            "and follow the official process outlined in the student handbook."
        )

    if "transfer" in text or "credit transfer" in text or "equivalent" in text:
        return (
            "If you have completed cybersecurity-related courses elsewhere, you may be able to transfer credits. Contact the registrar's office "
            "with your course transcripts and syllabus. They will evaluate whether the course is equivalent and can be credited toward your program. "
            "This usually takes a few weeks to process."
        )

    if "certificate" in text and ("completion" in text or "completion certificate" in text or "after course" in text):
        return (
            "Upon successful completion of the course, you will receive a course completion certificate or transcript entry showing your grade. "
            "This is usually available through the student portal or can be requested from the registrar. Keep copies for your records and job applications."
        )

    if "job placement" in text or "internship" in text or "career support" in text:
        return (
            "Some schools have career services that help students find internships and jobs. After completing the course, you may have access to "
            "job boards or alumni networks. Connect with industry professionals through networking events. Building a portfolio of your lab work can "
            "really help when applying for cybersecurity positions."
        )

    if "alumni" in text or "graduate" in text or "after graduation" in text:
        return (
            "Most schools maintain alumni networks with job boards, mentoring, and networking events. Staying connected can help with career growth "
            "and continuing education. Some alumni also return to guest lecture or mentor current students. Keep your alumni contact information updated."
        )

    # CAMPUS & FACILITIES
    if "campus" in text or "library" in text or "computer lab" in text or "facility" in text:
        return (
            "Campus facilities typically include a library, computer labs, student center, cafeteria, and recreational areas. Cybersecurity students often use "
            "dedicated lab spaces for hands-on practice. Check the campus map on the school website or ask student services for locations and opening hours."
        )

    if "accommodation" in text or "hostel" in text or "dorm" in text or "housing" in text:
        return (
            "If you need on-campus housing, contact the student affairs or accommodation office. If you prefer off-campus housing, check local listings or "
            "student housing groups. Start your search early as good options fill up quickly. Some schools have partnerships with landlords for student housing."
        )

    if "transportation" in text or "bus" in text or "parking" in text or "commute" in text:
        return (
            "Most schools offer public transportation passes or shuttles for students. Check if parking is available and what the fees are. Some cities also have "
            "student discounts on transit. Ask the student services office about your options when you arrive on campus."
        )

    if "health" in text or "medical" in text or "insurance" in text or "clinic" in text:
        return (
            "Most schools have a student health center providing basic medical services and vaccinations. International students often need health insurance. "
            "Check with student services about available health and wellness services. Keep emergency contact information updated."
        )

    if "fitness" in text or "gym" in text or "sports" in text or "recreation" in text:
        return (
            "Many schools offer free or subsidized gym access and sports facilities for students. Check the student center or athletics office for memberships and programs. "
            "Physical activity is great for stress relief while studying challenging subjects like cybersecurity!"
        )

    # ACADEMIC ADVISING & PLANNING
    if "advisor" in text or "academic advisor" in text or "guidance" in text:
        return (
            "Every student is assigned an academic advisor to help with course selection and degree planning. Meet with them at least once per semester. "
            "They can answer questions about prerequisites, course sequencing, and career paths. Don't hesitate to ask for advice—that's what they're there for!"
        )

    if "major" in text or "specialization" in text or "focus area" in text:
        return (
            "Some schools allow cybersecurity students to choose specializations like ethical hacking, network defense, or incident response. Discuss specialization options "
            "with your academic advisor early so you can plan your electives accordingly."
        )

    if "course load" in text or "how many courses" in text or "full time" in text:
        return (
            "A typical full-time course load is 4-6 courses per semester, but this varies by school and program. Check your course registration page or ask your advisor "
            "about recommended course loads based on your goals and background. Balancing coursework with work or personal commitments is important."
        )

    if "prerequisite" in text and "check" in text:
        return (
            "Check the course catalog or your student portal to see prerequisites for each course. Prerequisites ensure you have necessary knowledge before advancing. "
            "If you're unsure whether you meet a prerequisite, contact the course instructor or your department."
        )

    # LEARNING METHODS & ASSESSMENT
    if "online exam" in text or "proctored" in text or "monitoring" in text:
        return (
            "Online exams may be proctored using webcam monitoring or exam software. Some require you to take the exam in a testing center on campus. Your course syllabus "
            "will explain the exam format and requirements. Set up your technology properly to avoid technical issues during exams."
        )

    if "open book" in text or "closed book" in text or "cheat" in text or "academic integrity" in text:
        return (
            "Academic integrity is crucial in cybersecurity education. Understand your school's honor code and what constitutes cheating. Most exams specify whether "
            "books or notes are allowed. Plagiarism and unauthorized collaboration are serious offenses. Always cite your sources and do your own work."
        )

    if "midterm" in text or "final exam" in text or "cumulative" in text:
        return (
            "Midterms usually cover material from the first half of the semester, while final exams are often cumulative, covering the entire course. Check your syllabus "
            "for exam dates and what topics will be covered. Start studying early and review previous assignments and class notes."
        )

    if "pass fail" in text or "retake" in text or "repeat course" in text:
        return (
            "Some schools offer pass/fail grading for certain courses or allow students to retake courses if they perform poorly. Check your institution's policies. "
            "Retaking a course may replace the old grade or appear as a separate entry on your transcript. Talk to your advisor about your options."
        )

    # TECHNICAL & PREREQUISITES
    if "computer" in text and ("requirements" in text or "specs" in text or "minimum" in text):
        return (
            "For cybersecurity labs, you typically need a laptop or desktop with 8-16GB RAM, modern processor, and reliable internet. Windows, Mac, or Linux are all acceptable. "
            "You may also need to install virtual machines or specific software. Check your course requirements or contact your instructor for exact specifications."
        )

    if "internet" in text or "bandwidth" in text or "connection" in text or "wifi" in text:
        return (
            "A reliable broadband internet connection (minimum 5-10 Mbps) is essential for online classes and lab work. Download large lab files in advance if possible. "
            "If you have connectivity issues, notify your instructor immediately. Most schools have Wi-Fi available on campus and in libraries."
        )

    if "software" in text or "kali linux" in text or "virtual machine" in text or "vmware" in text:
        return (
            "Cybersecurity labs often use tools like Kali Linux, VirtualBox, or VMware. Some software is free, others require paid licenses. Your institution may provide "
            "licenses or lab access. Download and install required software before the course begins, or contact IT support for help."
        )

    if "password manager" in text or "two factor" in text or "2fa" in text or "mfa" in text:
        return (
            "Use strong, unique passwords and enable two-factor authentication on important accounts like your student portal. Consider using a password manager to keep "
            "track of passwords securely. This is a cybersecurity best practice you'll learn in the course—start practicing now!"
        )

    # REAL-WORLD SCENARIOS & SECURITY
    if "data breach" in text or "ransomware" in text or "phishing" in text or "malware" in text:
        return (
            "Data breaches and cyberattacks happen daily in the real world. Ransomware locks files, phishing tricks users into revealing information, and malware damages systems. "
            "Learning cybersecurity helps protect against these threats. This course teaches you how to recognize and prevent such attacks."
        )

    if "ransomware" in text and "what" in text:
        return (
            "Ransomware is malicious software that encrypts your files and demands payment to decrypt them. It spreads through phishing emails or security vulnerabilities. "
            "Prevention includes: regular backups, software updates, security training, and firewalls. If infected, never pay the ransom."
        )

    if "security breach" in text or "compromised" in text or "account hacked" in text:
        return (
            "If your account is compromised: change your password immediately, enable two-factor authentication, review account activity, and notify support. "
            "For institutional accounts, contact IT support. Learn from the course how to prevent breaches through strong passwords, backup authentication, and vigilance."
        )

    if "vpn" in text or "proxy" in text or "tor" in text or "anonymity" in text:
        return (
            "A VPN encrypts your internet traffic and masks your IP address for privacy. It's useful on public Wi-Fi networks. However, VPNs don't make you completely anonymous. "
            "Some institutions restrict VPN use on campus networks. Only use legal VPN services from trusted providers."
        )

    if "firewall" in text or "antivirus" in text or "antimalware" in text:
        return (
            "A firewall controls incoming/outgoing network traffic, while antivirus software detects and removes malicious files. Both are essential for computer security. "
            "Keep your antivirus updated and enable Windows Defender or a reputable third-party option. These topics are covered in depth in the cybersecurity course."
        )

    if "backup" in text or "data recovery" in text or "disaster recovery" in text:
        return (
            "Regular backups are critical—if ransomware hits or hardware fails, you lose nothing. Use cloud services, external drives, or both. Follow the 3-2-1 rule: "
            "3 copies of data, 2 different media types, 1 copy offsite. Your institution likely has backup policies for important data."
        )

    if "social engineering" in text or "pretexting" in text or "social manipulation" in text:
        return (
            "Social engineering is manipulating people into revealing confidential information or performing security mistakes. Examples: fake helpful calls, fake login pages, "
            "or urgent emails from 'authority.' The best defense is skepticism, verification, and security awareness—all taught in cybersecurity courses."
        )

    if "zero trust" in text or "least privilege" in text or "defense in depth" in text:
        return (
            "Modern security strategies include: Zero Trust (verify everything), Least Privilege (minimum access needed), and Defense in Depth (multiple security layers). "
            "These concepts reduce risk even if one security measure fails. You'll study these frameworks in depth during the course."
        )

    # INDUSTRY & CERTIFICATIONS DEEP DIVE
    if "comptia" in text or "security plus" in text or "sec+" in text:
        return (
            "CompTIA Security+ is an industry-standard certification covering security administration, threat management, and cryptography. It requires 5 years of IT experience "
            "(or an equivalent certification) or 2 years with CompTIA Network+. This course prepares you for Security+."
        )

    if "cissp" in text or "oscp" in text or "cism" in text or "advanced certification" in text:
        return (
            "Advanced certifications like CISSP, OSCP, and CISM require significant experience and study. CISSP is for security architects, OSCP is for penetration testers, "
            "and CISM is for IT managers. Start with beginner certs like Security+ and build up from there."
        )

    if "bug bounty" in text or "responsible disclosure" in text or "vulnerability reporting" in text:
        return (
            "Bug bounty programs reward hackers for finding security vulnerabilities responsibly. You report bugs to the company before public disclosure, giving time to patch. "
            "This is a legal way to practice hacking skills while helping organizations. Never hack without permission."
        )

    if "penetration test" in text or "pen test" in text or "authorized" in text:
        return (
            "A penetration test (pen test) is an authorized security audit where experts attempt to breach systems to find weaknesses. It's completely legal when you have written "
            "permission. Companies hire pen testers to test their security before real attackers find vulnerabilities."
        )

    if "soc analyst" in text or "security operations" in text or "incident response" in text:
        return (
            "A Security Operations Center (SOC) analyst monitors networks for security incidents 24/7. When breaches occur, incident response teams investigate and contain "
            "damage. These are growing careers with good salaries. Your course provides foundational knowledge for SOC roles."
        )

    if "devops" in text or "devsecops" in text or "secure development" in text:
        return (
            "DevSecOps integrates security into software development from the start. Developers build secure code, automated tests catch vulnerabilities, and security teams "
            "collaborate throughout. This approach reduces security issues in production systems."
        )

    # COMMON MISCONCEPTIONS
    if ("black hat" in text or "white hat" in text or "grey hat" in text) and ("hacker" in text or "hacking" in text):
        return (
            "White hat hackers (ethical hackers) test security with permission. Black hat hackers attack illegally for personal gain. Grey hats are in between—finding bugs "
            "without permission but not for profit. This course teaches white hat (ethical) hacking only."
        )

    if "impossible" in text or "too difficult" in text or "can't do it" in text:
        return (
            "Many students worry cybersecurity is impossible before starting. But thousands of students—from different backgrounds—complete cybersecurity courses successfully. "
            "It's challenging but definitely doable with consistent effort, good study habits, and asking for help when needed."
        )

    if "background" in text and ("it" in text or "computer" in text or "programming" in text):
        return (
            "You don't need an IT or programming background to start cybersecurity. Many successful professionals switched careers into security. Starting with basics and building "
            "gradually works well. Your course starts with fundamentals specifically for beginners like you."
        )

    if "age" in text or "too old" in text or "too young" in text:
        return (
            "Cybersecurity welcomes people of all ages. Career changers in their 40s and 50s succeed, as do recent high school graduates. Security teams value diverse perspectives. "
            "If you're interested, you're the right age to learn."
        )

    # STUDY STRATEGIES & TIME MANAGEMENT
    if "procrastination" in text or "motivation" in text or "falling behind" in text:
        return (
            "Set a regular study schedule and stick to it, even if just 1-2 hours daily. Break assignments into smaller tasks with mini-deadlines. Join study groups for accountability. "
            "If motivation drops, remember your goals. Email your instructor if you're struggling—they want to help."
        )

    if "stress" in text or "overwhelm" in text or "anxiety" in text or "mental health" in text:
        return (
            "Cybersecurity is demanding but manageable with healthy habits: exercise, good sleep, balanced meals, and breaks. Use campus mental health services if stress becomes overwhelming. "
            "Many students feel overwhelmed sometimes—you're not alone. Reach out for support."
        )

    if "study group" in text or "peer study" in text or "classmate" in text:
        return (
            "Study groups are powerful for learning and motivation. Find classmates to study with on labs, quizzes, and projects. Teaching others reinforces your own understanding. "
            "Many cybersecurity students connect through online forums or Discord servers too."
        )

    if "note" in text or "flashcard" in text or "spaced repetition" in text or "active recall" in text:
        return (
            "Effective study methods include: Cornell note-taking, active recall (testing yourself), spaced repetition (reviewing at intervals), and teaching others. "
            "Digital flashcards like Anki work well for memorizing security concepts and tools. Experiment to find what works for you."
        )

    if "sleep" in text or "all nighter" in text or "tired" in text:
        return (
            "Adequate sleep (7-9 hours) improves learning and memory far more than all-nighters. Tired brains can't learn complex cybersecurity concepts well. Plan ahead so you "
            "don't need to cram. You'll retain more and perform better with good sleep."
        )

    # PRACTICAL SKILLS & LABS
    if "linux" in text and "command" in text:
        return (
            "Linux command line is essential in cybersecurity. Learn basic commands: ls, cd, grep, chmod, sudo. Practice regularly in your lab environment. Many security tools run on Linux. "
            "The course teaches Linux basics step by step."
        )

    if "networking" in text and ("tcp" in text or "ip" in text or "protocol" in text):
        return (
            "Networking fundamentals include: IP addresses, TCP/IP protocols, DNS, firewalls, and routing. Understanding networks is crucial for cybersecurity. Your course covers these basics "
            "needed to understand network attacks and defenses."
        )

    if "scripting" in text and ("bash" in text or "python" in text or "powershell" in text):
        return (
            "Scripting automates security tasks. Bash (Linux shell), Python, and PowerShell are commonly used. You don't need to be a programmer, but basic scripting helps. "
            "The course introduces scripting and most students learn it during labs without prior experience."
        )

    if "database" in text or "sql" in text or "sql injection" in text:
        return (
            "Databases store sensitive data. SQL is the language for querying databases. SQL injection is a common attack where attackers insert malicious SQL commands. "
            "Your course teaches database security basics and real-world attack scenarios."
        )

    if "encryption" in text and ("rsa" in text or "aes" in text or "bcrypt" in text):
        return (
            "Encryption protects data using mathematical algorithms. RSA and AES are common encryption algorithms. Understanding how encryption works helps you protect data properly. "
            "Cryptography is covered in your cybersecurity course."
        )

    # INDUSTRY FACTS & TRENDS
    if "salary" in text and ("cybersecurity" in text or "security analyst" in text or "income" in text):
        return (
            "Cybersecurity professionals earn competitive salaries. Entry-level positions start around $50-70K, while experienced roles earn $100K+. Salaries vary by country, "
            "location, company size, and specialization. The demand is growing faster than talent supply, so opportunities are excellent."
        )

    if "job market" in text or "demand" in text or "shortage" in text or "hiring" in text:
        return (
            "The cybersecurity job market is booming. Companies urgently need security professionals but can't find enough. This shortage means good job security and opportunities "
            "for career growth. Completing this course positions you well for employment in this growing field."
        )

    if "remote" in text or "work from home" in text or "flexible location" in text:
        return (
            "Many cybersecurity roles offer remote or hybrid options. Security analysis, threat intelligence, and some development roles work well remotely. Some positions require "
            "on-site presence for network management. Ask about work arrangements during interviews."
        )

    if "company" in text or "tech companies" in text or "industries" in text or "employer" in text:
        return (
            "Cybersecurity jobs exist in all industries: technology, finance, healthcare, government, retail, energy, etc. Big tech companies, banks, hospitals, and startups all hire security people. "
            "Any organization handling sensitive data needs cybersecurity professionals."
        )

    if "future" in text or "emerging" in text or "trend" in text or "ai security" in text or "cloud security" in text:
        return (
            "Emerging areas in cybersecurity include: AI/ML security, cloud security, IoT security, and blockchain. Learning fundamentals now prepares you for future specializations. "
            "The field evolves constantly, so continuous learning is essential throughout your career."
        )

    # ROOT CAUSE SCENARIOS
    if "forgot password" in text or "account locked" in text or "cannot access" in text:
        return (
            "If you forgot your password, use the 'Forgot Password' link on the portal login page. You'll reset it via email. If your account is locked after failed login attempts, "
            "contact the ICT helpdesk. Keep your recovery email updated and use a password manager to avoid forgetting passwords."
        )

    if "lab down" in text or "lab not working" in text or "lab access denied" in text or "error" in text:
        return (
            "If labs aren't working, check: 1) Your internet connection, 2) Browser compatibility, 3) Software requirements met. Clear browser cache and try again. "
            "If still failing, take a screenshot of the error and email your instructor or ICT support immediately."
        )

    if "browser" in text and ("not compatible" in text or "not supporting" in text or "doesn't work" in text):
        return (
            "Try a modern browser: Chrome, Firefox, Safari, or Edge. Labs usually require updated browsers. Disable browser extensions if they interfere. Ensure JavaScript is enabled. "
            "Test labs on a different device if available to verify it's not your specific setup."
        )

    if "notification" in text or "email" in text or "not receiving" in text or "missed" in text:
        return (
            "Check your school email regularly—important course announcements go there. Check spam/junk folders for legitimate emails. Ask to be added to course mailing lists if available. "
            "Enable notifications on the student portal to see announcements immediately."
        )

    # MOTIVATION & SUCCESS STORIES
    if "success" in text or "graduate student" in text or "completed course" in text or "finished" in text:
        return (
            "Many students complete this course successfully and proceed to great careers in cybersecurity. Success comes from consistent effort, asking for help, and staying curious. "
            "Your determination to learn and grow is what matters most. You can do this!"
        )

    if "stuck" in text or "confused" in text or "help" in text and "understand" in text:
        return (
            "If you're confused about something, don't suffer alone! Options: 1) Reread the course material, 2) Watch explanation videos, 3) Ask classmates in study groups, "
            "4) Email your instructor, 5) Visit office hours, 6) Seek tutoring. Getting help early prevents further confusion."
        )

    if "pass" in text or "succeed" in text or "win" in text or "confident" in text:
        return (
            "Your success in this course depends on consistent effort, curiosity, and persistence. Study regularly, complete labs thoroughly, ask questions, and practice. "
            "You have everything you need to succeed. Believe in yourself and take it one topic at a time!"
        )

    # DEFAULT
    return "I'm not sure I understand. Could you rephrase? Or type 'help' to see what I can assist with."

def main():
    print_welcome()
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() in {"exit", "quit", "bye", "goodbye"}:
                print(f"Bot: {get_response(user_input)}")
                break
            response = get_response(user_input)
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            print("\n\nBot: Thank you for chatting. Goodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
