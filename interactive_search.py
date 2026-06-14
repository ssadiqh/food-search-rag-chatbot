"""Interactive CLI Food Search System"""
# -*- coding: utf-8 -*-
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from shared_functions import *

food_items = []


def main():
    """Main function for interactive CLI food recommendation system"""
    try:
        print("\n" + "="*60)
        print("🍽️  INTERACTIVE FOOD RECOMMENDATION SYSTEM")
        print("="*60)
        print("Loading food database...")

        global food_items
        food_items = load_food_data('./FoodDataSet.json')

        collection = create_similarity_search_collection(
            "interactive_food_search",
            {'description': 'Interactive food search collection'}
        )
        populate_similarity_collection(collection, food_items)

        interactive_food_chatbot(collection)

    except Exception as error:
        print(f"❌ Error: {error}")


def interactive_food_chatbot(collection):
    """Interactive CLI chatbot for food recommendations"""
    print("\n" + "="*60)
    print("🤖 FOOD SEARCH CHATBOT")
    print("="*60)
    print("Commands:")
    print("  • Type food name or description to search")
    print("  • 'help' - Show available commands")
    print("  • 'quit' - Exit the system")
    print("-" * 60)

    while True:
        try:
            user_input = input("\n🔍 Search for food: ").strip()

            if not user_input:
                print("   Please enter a search term")
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you! Goodbye!")
                break

            elif user_input.lower() in ['help', 'h']:
                show_help_menu()

            else:
                handle_food_search(collection, user_input)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def show_help_menu():
    """Display help information"""
    print("\n📖 HELP MENU")
    print("-" * 40)
    print("Search Examples:")
    print("  • 'chocolate dessert' - Find chocolate desserts")
    print("  • 'Italian food' - Find Italian cuisine")
    print("  • 'sweet treats' - Find sweet desserts")
    print("  • 'low calorie' - Find lighter options")
    print("\nCommands:")
    print("  • 'help' - Show this menu")
    print("  • 'quit' - Exit the system")


def handle_food_search(collection, query):
    """Handle food similarity search"""
    print(f"\n🔍 Searching for '{query}'...")

    results = perform_similarity_search(collection, query, 5)

    if not results:
        print("❌ No matching foods found")
        print("💡 Try different keywords")
        return

    print(f"\n✅ Found {len(results)} recommendations:")
    print("=" * 70)

    for i, result in enumerate(results, 1):
        percentage_score = result['similarity_score'] * 100

        print(f"\n{i}. 🍽️  {result['food_name']}")
        print(f"   📊 Match Score: {percentage_score:.1f}%")
        print(f"   🏷️  Cuisine: {result['cuisine_type']}")
        print(f"   🔥 Calories: {result['food_calories_per_serving']} per serving")
        print(f"   📝 {result['food_description']}")

        if i < len(results):
            print("   " + "-" * 60)

    print("=" * 70)

    suggest_related_searches(results)


def suggest_related_searches(results):
    """Suggest related searches"""
    if not results:
        return

    cuisines = list(set([r['cuisine_type'] for r in results]))

    print("\n💡 Related searches:")
    for cuisine in cuisines[:3]:
        print(f"   • Try '{cuisine} dishes'")


if __name__ == "__main__":
    main()