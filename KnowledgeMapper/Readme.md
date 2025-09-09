# KnowledgeMapper

KnowledgeMapper is a Python tool that generates a mind map from the section structure of a Wikipedia page for a given topic. It outputs both a text-based mind map in the console and a graphical mind map image using Graphviz.

## Features
- Fetches section headers (`h2`, `h3`) from any Wikipedia page
- Prints a hierarchical mind map in the console
- Generates a mind map image (`mindmap.png`) using Graphviz

## Requirements
- Python 3.x
- requests
- beautifulsoup4
- pygraphviz
- Graphviz (system package)

## Installation
1. Install required Python packages:
   ```powershell
   pip install requests beautifulsoup4 pygraphviz
   ```
2. Download and install [Graphviz](https://graphviz.gitlab.io/download/).
   - Add Graphviz executables to your system PATH.

## Usage
Edit the `topic` variable in `Code.py` to your desired Wikipedia topic:
```python
if __name__ == "__main__":
    topic = "Machine learning"  # Change to any Wikipedia topic
    sections = fetch_wikipedia_sections(topic)
    print(f"\nMindMap for: {topic}\n")
    print_mindmap(sections)
    save_mindmap_graph(sections, topic)
    print("\nMindmap saved as mindmap.png")
```
Run the script:
```powershell
python Code.py
```

## Output
- Console: Hierarchical mind map of Wikipedia sections
- File: `mindmap.png` (graphical mind map)

## Notes
- Only `h2` and `h3` sections are mapped.
- Requires internet access to fetch Wikipedia pages.
- Graphviz must be installed and available in PATH for image generation.

## License
This project is provided for educational purposes.