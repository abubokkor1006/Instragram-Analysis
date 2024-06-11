def analyze_followers(followers):
    total_followers = len(followers)
    print("Total number of followers:", total_followers)
    
    # Calculate average number of followers
    total_followers_count = sum(followers.values())
    average_followers = total_followers_count / total_followers
    print("Average number of followers:", average_followers)
    
    # Find most popular follower
    most_popular = max(followers, key=followers.get)
    most_popular_followers = followers[most_popular]
    print("Most popular follower:", most_popular, "with", most_popular_followers, "followers")

    # Find least popular follower
    least_popular = min(followers, key=followers.get)
    least_popular_followers = followers[least_popular]
    print("Least popular follower:", least_popular, "with", least_popular_followers, "followers")

if __name__ == "__main__":
    # Sample followers data (replace with your own)
    followers = {
        "user1": 1000,
        "user2": 500,
        "user3": 2000,
        "user4": 300,
        "user5": 1500
    }
    
    # Analyze followers
    analyze_followers(followers)