for $doc in collection('recipe')
where $doc/recipeml/recipe/head/yield > 20
return <p><a href="getRecipe.xqy?recipeName={document-uri($doc)}">{$doc/recipeml/recipe/head/title/text()}</a></p>
