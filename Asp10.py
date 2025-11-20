def find_partners(N, X, skills):
    partners = [i + 1 for i, skill in enumerate(skills) if skill >= X]
    return partners

def main():
    try:
        N = int(input())
        X = int(input())
        skills = [int(input()) for _ in range(N)]
        partners = find_partners(N, X, skills)
        if partners:
            print("Partners are:", partners)
        else:
            print("No partners found")
    except Exception as e:
        # In a real application, you'd log this error
        pass

if __name__ == "__main__":
    main()