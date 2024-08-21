import requests
from bs4 import BeautifulSoup

def get_courses_by_url(url):
    try:
        # Sending an HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using beautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        course_list = soup.find_all('li')  # Target the list element 
        
        if not course_list:
            return "No courses found or unable to locate the course list on the webpage."

        # Extract the course names
        courses = [li.get_text(strip=True) for li in course_list]

        return courses if courses else "No courses found on the page."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def scrape_college_courses(college_name, url):
    print(f"Scraping courses for {college_name}...")
    courses = get_courses_by_url(url)
    if isinstance(courses, list):
        print(f"Courses offered by {college_name}:")
        for course in courses:
            print(f"- {course}")
    else:
        print(f"Error for {college_name}: {courses}")
    print("\n")
    

# College URLs from Delhi University
colleges = {
    "St. Stephen's College": "https://www.ststephens.edu/courses/",
    "Hindu College": "https://hinducollege.ac.in/acd-departments.aspx",
    "Sri Venkateswara College": "https://www.vivekanandacollege.edu.in/academics/courses",
    "Miranda House": "https://www.mirandahouse.ac.in/courses.php",
    "Lady Shri Ram College for Women (LSR)": "https://lsr.edu.in/admissions/courses-offered/",
    "Ramjas College": "https://ramjas.du.ac.in/college/web/index.php?r=ug-courses",
    "Kirori Mal College": "https://ramjas.du.ac.in/college/web/index.php?r=ug-courses",
    "Hansraj College": "https://ramjas.du.ac.in/college/web/index.php?r=ug-courses"
}

# Iterate over the dictionary and scrape courses for each college
for college_name, url in colleges.items():
    scrape_college_courses(college_name, url)
