from datetime import date, time

from pawpal_system import Owner, Pet, Task, TaskCategory, Scheduler


def main():
    owner = Owner(name="Jay", age=30)

    # Add pets
    dog = Pet(name="Sunny", age=4, species="Dog", breed="Golden Retriever")
    cat = Pet(name="Mittens", age=2, species="Cat", breed="Tabby")
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Add tasks
    dog.add_task(Task(
        title="Morning walk",
        description="30-minute walk around the block",
        duration_minutes=30,
        priority=5,
        category=TaskCategory.WALK,
        preferred_time=time(hour=8, minute=0)
    ))

    dog.add_task(Task(
        title="Evening fetch",
        description="15-minute fetch session",
        duration_minutes=15,
        priority=3,
        category=TaskCategory.ENRICHMENT,
        preferred_time=time(hour=17, minute=30)
    ))

    cat.add_task(Task(
        title="Feeding",
        description="Give wet and dry food",
        duration_minutes=10,
        priority=4,
        category=TaskCategory.FEED,
        preferred_time=time(hour=7, minute=30)
    ))

    cat.add_task(Task(
        title="Litter clean",
        description="Scoop litter box",
        duration_minutes=10,
        priority=2,
        category=TaskCategory.GROOMING,
        preferred_time=time(hour=18, minute=0)
    ))

    scheduler = Scheduler(owner=owner, date=date.today())
    scheduler.generate_daily_plan()
    print(scheduler.explain_plan())
    print("\nSummary:", scheduler.get_summary())


if __name__ == "__main__":
    main()
