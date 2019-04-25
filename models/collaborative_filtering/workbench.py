from recommendations import critics
print(critics['Lisa Rose'])

# check two types of similarity metrics
import recommendations
print(recommendations.sim_distance(recommendations.critics, 'Lisa Rose','Gene Seymour'))
print(recommendations.sim_pearson(recommendations.critics, 'Lisa Rose','Gene Seymour'))

# rank most similar users
print(recommendations.topMatches(recommendations.critics,'Toby',n=3))

# rank most similar items
movies=recommendations.transformPrefs(recommendations.critics)
print(recommendations.topMatches(movies,'Superman Returns'))

# recommend items to user
print(recommendations.getRecommendations(recommendations.critics,'Toby'))
print(recommendations.getRecommendations(recommendations.critics,'Toby', similarity=recommendations.sim_distance))

# recommend users for movie
print(recommendations.getRecommendations(movies,'Just My Luck'))

itemsim = recommendations.calculateSimilarItems(recommendations.critics)
print(itemsim)
print(recommendations.getRecommendedItems(recommendations.critics,itemsim,'Toby'))