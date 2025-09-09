import requests
from bs4 import BeautifulSoup
import pygraphviz as pgv

def fetch_wikipedia_sections(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    sections = []
    for header in soup.find_all(['h2', 'h3']):
        title = header.text.strip().replace('[edit]', '')
        sections.append((header.name, title))
    return sections

def print_mindmap(sections):
    stack = []
    for tag, title in sections:
        indent = "    " * (int(tag[1]) - 2)
        print(f"{indent}├── {title}")

def save_mindmap_graph(sections, topic):
    G = pgv.AGraph(directed=True)
    last_h2 = None
    for tag, title in sections:
        if tag == "h2":
            G.add_edge(topic, title)
            last_h2 = title
        elif tag == "h3" and last_h2:
            G.add_edge(last_h2, title)
    G.layout(prog='dot')
    G.draw("mindmap.png")

if __name__ == "__main__":
    topic = "Machine learning"
    sections = fetch_wikipedia_sections(topic)
    print(f"\nMindMap for: {topic}\n")
    print_mindmap(sections)
    save_mindmap_graph(sections, topic)
    print("\nMindmap saved as mindmap.png")
