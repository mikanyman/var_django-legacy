(: Create an HTML page linking to recipes  
   that serve more than 20 people.         :)

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Food for a Crowd</title></head>
<body>

  <h1>Food for a Crowd</h1>
<div xmlns="">
  { 
  for $doc in collection('recipes')
    where $doc/recipeml/recipe/head/yield > 20 
      return <p><a href="getRecipe.xqy?recipeName={document-uri($doc)}">
        {$doc/recipeml/recipe/head/title/text()}</a>
      </p>
  }
</div>
</body></html>


