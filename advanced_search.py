"""Advanced Food Search System with Filtering"""
# -*- coding: utf-8 -*-
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from shared_functions import *


def main():
    """Main function for advanced search system"""
    try:
        print("\n" + "="*60)
        print("🔬 ADVANCED FOOD SEARCH SYSTEM")
        print("="*60)
        print("Loading food database with filtering...")

        food_items = load_food_data('./FoodDataSet.json')

        collection = create_similarity_search_collection(
            "advanced_food_search",
            {'description': 'Advanced search with filters'}
        )
        populate_similarity_collection(collection, food_items)

        interactive_advanced_search(collection)

    except Exception as error:
        print(f"❌ Error: {error}")


def interactive_advanced_search(collection):
    """Interactive advanced search menu"""
    print("\n" + "="*60)
    print("🔧 ADVANCED SEARCH OPTIONS")
    print("="*60)
    print("1. Basic similarity search")
    print("2. Cuisine-filtered search")
    print("3. Calorie-filtered search")
    print("4. Combined filters search")
    print("5. Demonstration mode")
    print("6. Help")
    print("7. Exit")
    print("-" * 60)

    while True:
        try:
            choice = input("\n📋 Select option (1-7): ").strip()

            if choice == '1':
                perform_basic_search(collection)
            elif choice == '2':
                perform_cuisine_filtered_search(collection)
            elif choice == '3':
                perform_calorie_filtered_search(collection)
            elif choice == '4':
                perform_combined_filtered_search(collection)
            elif choice == '5':
                run_search_demonstrations(collection)
            elif choice == '6':
                show_advanced_help()
            elif choice == '7':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid option")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def perform_basic_search(collection):
    """Basic similarity search"""
    print("\n🔍 BASIC SEARCH")
    print("-" * 40)
    query = input("Enter search query: ").strip()
    if not query:
        print("❌ Please enter a search term")
        return

    results = perform_similarity_search(collection, query, 5)
    display_search_results(results, "Basic Search Results")


def perform_cuisine_filtered_search(collection):
    """Cuisine-filtered search"""
    print("\n🍽️ CUISINE-FILTERED SEARCH")
    print("-" * 40)

    cuisines = ["Italian", "Thai", "Mexican", "Indian", "Japanese",
                "French", "Mediterranean", "American", "Asian", "Dessert"]
    print("Available cuisines:")
    for i, cuisine in enumerate(cuisines, 1):
        print(f"  {i}. {cuisine}")

    query = input("\nEnter search query: ").strip()
    cuisine_choice = input("Enter cuisine number: ").strip()

    if not query:
        print("❌ Please enter a search term")
        return

    cuisine_filter = None
    if cuisine_choice.isdigit():
        idx = int(cuisine_choice) - 1
        if 0 <= idx < len(cuisines):
            cuisine_filter = cuisines[idx]

    if not cuisine_filter:
        print("❌ Invalid cuisine selection")
        return

    results = perform_filtered_similarity_search(
        collection, query, cuisine_filter=cuisine_filter, n_results=5
    )
    display_search_results(results, f"Cuisine-Filtered Results ({cuisine_filter})")


def perform_calorie_filtered_search(collection):
    """Calorie-filtered search"""
    print("\n🔥 CALORIE-FILTERED SEARCH")
    print("-" * 40)

    query = input("Enter search query: ").strip()
    max_cal_input = input("Enter max calories (or press Enter for no limit): ").strip()

    if not query:
        print("❌ Please enter a search term")
        return

    max_calories = None
    if max_cal_input.isdigit():
        max_calories = int(max_cal_input)

    results = perform_filtered_similarity_search(
        collection, query, max_calories=max_calories, n_results=5
    )
    calorie_text = f"under {max_calories} calories" if max_calories else "any calories"
    display_search_results(results, f"Calorie-Filtered Results ({calorie_text})")


def perform_combined_filtered_search(collection):
    """Search with multiple filters"""
    print("\n🎯 COMBINED FILTERS SEARCH")
    print("-" * 40)

    query = input("Enter search query: ").strip()
    cuisine = input("Enter cuisine type (optional): ").strip()
    max_cal = input("Enter max calories (optional): ").strip()

    if not query:
        print("❌ Please enter a search term")
        return

    cuisine_filter = cuisine if cuisine else None
    max_calories = int(max_cal) if max_cal.isdigit() else None

    results = perform_filtered_similarity_search(
        collection, query,
        cuisine_filter=cuisine_filter,
        max_calories=max_calories,
        n_results=5
    )
    filters = []
    if cuisine_filter:
        filters.append(f"cuisine: {cuisine_filter}")
    if max_calories:
        filters.append(f"max: {max_calories} cal")
    filter_text = ", ".join(filters) if filters else "no filters"

    display_search_results(results, f"Combined Results ({filter_text})")


def run_search_demonstrations(collection):
    """Run demonstration searches"""
    print("\n📊 DEMONSTRATIONS")
    print("=" * 50)

    demos = [
        {"title": "Italian Cuisine", "query": "creamy pasta", "cuisine": "Italian", "cal": None},
        {"title": "Low-Calorie", "query": "healthy meal", "cuisine": None, "cal": 300},
        {"title": "Japanese Light", "query": "light fresh", "cuisine": "Japanese", "cal": 250}
    ]

    for i, demo in enumerate(demos, 1):
        print(f"\n{i}. {demo['title']}")
        print(f"   Query: '{demo['query']}'")

        filters = []
        if demo['cuisine']:
            filters.append(f"Cuisine: {demo['cuisine']}")
        if demo['cal']:
            filters.append(f"Max: {demo['cal']} cal")
        if filters:
            print(f"   Filters: {', '.join(filters)}")

        results = perform_filtered_similarity_search(
            collection, demo['query'],
            cuisine_filter=demo['cuisine'],
            max_calories=demo['cal'],
            n_results=3
        )

        display_search_results(results, demo['title'], show_details=False)
        input("\n⏸️  Press Enter to continue...")


def display_search_results(results, title, show_details=True):
    """Display formatted results"""
    print(f"\n📋 {title}")
    print("=" * 60)

    if not results:
        print("❌ No matching results found")
        return

    for i, result in enumerate(results, 1):
        score = result['similarity_score'] * 100

        if show_details:
            print(f"\n{i}. 🍽️  {result['food_name']}")
            print(f"   📊 Score: {score:.1f}%")
            print(f"   🏷️  {result['cuisine_type']}")
            print(f"   🔥 {result['food_calories_per_serving']} cal")
            print(f"   📝 {result['food_description']}")
        else:
            print(f"   {i}. {result['food_name']} ({score:.1f}%)")

    print("=" * 60)


def show_advanced_help():
    """Display help information"""
    print("\n📖 HELP")
    print("=" * 40)
    print("Search Types:")
    print("  1. Basic - Standard similarity search")
    print("  2. Cuisine - Filter by cuisine type")
    print("  3. Calorie - Filter by calorie limit")
    print("  4. Combined - Use multiple filters")
    print("\nTips:")
    print("  • Use descriptive terms")
    print("  • Combine ingredients")
    print("  • Try cuisine names")


if __name__ == "__main__":
    main()