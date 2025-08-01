import { useEffect } from 'react'
import { RecipeList } from '../componenets/RecipeList'
import { useNavigate } from 'react-router-dom';

export function Home({recipes, setRecipes, currentRecipe, setCurrentRecipe}) {

    const navigate = useNavigate();

    // whenever we return to the home page, refresh the recipe list
    useEffect(() => {
        fetchRecipes()
    }, []);    

    const fetchRecipes = async () => {
        const response = await fetch("http://127.0.0.1:5000/recipes")
        const data = await response.json()
        setRecipes(data.recipes)    
        console.log(data.recipes)
    }

    const openEditPage = (recipe) => {
        setCurrentRecipe(recipe)
        navigate('/edit_recipe')
    } 

  return (
    <div>
      <h1>Everybody Eats</h1>  
        <RecipeList recipes={recipes} updateRecipe={openEditPage} updateCallback={fetchRecipes}/>
    </div>
  );
}