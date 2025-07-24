import { useState, useEffect } from 'react'
import './App.css'
import RecipeList from './RecipeList'
import RecipeForm from './RecipeForm'

function App() {

  const [recipes, setRecipes] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentRecipe, setCurrentRecipe] = useState({})

  useEffect(() => {
    fetchRecipes()
  }, []);

  const fetchRecipes = async () => {
    const response = await fetch("http://127.0.0.1:5000/recipes")
    const data = await response.json()
    setRecipes(data.recipes)    
    console.log(data.recipes)
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentRecipe({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (recipe) => {
    if (isModalOpen) return
    setCurrentRecipe(recipe)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchRecipes()
  }


  return (
    <>
      <RecipeList recipes={recipes} updateRecipe={openEditModal} updateCallback={onUpdate}/>
      <button onClick={openCreateModal}>Create New Recipe</button>
      {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span> 
          <RecipeForm existingRecipe={currentRecipe} updateCallback={onUpdate}/> 
        </div>
      </div>

      }
    </>
  );
}

export default App
