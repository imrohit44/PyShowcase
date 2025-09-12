import time, random
words = ["python", "crawler", "unique", "mindmap", "speed", "typing", "snake"]

sample = " ".join(random.choices(words, k=8))
print("Type this:\n", sample)

start = time.time()
typed = input("\nYour input:\n")
end = time.time()

speed = len(sample.split()) / ((end - start)/60)
print(f"\nWPM: {speed:.2f}")
