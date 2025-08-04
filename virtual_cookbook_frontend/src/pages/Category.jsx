import { useEffect, useState } from 'react'
import { RecipeList } from '../componenets/RecipeList'
import { useNavigate } from 'react-router-dom';

export function Category({recipes, setRecipes, currentRecipe, setCurrentRecipe}) {

    const [filteredRecipes, setFilteredRecipes] = useState([])

    useEffect(() => {
        fetchRecipes()
    }, []);    

    const fetchRecipes = async () => {
        const response = await fetch("http://127.0.0.1:5000/breakfast")
        const data = await response.json()
        setRecipes(data.recipes)    
        console.log(data.recipes)
    }    

    return (
        <>
            <RecipeList recipes={recipes}/>
        
        </>
    )
}