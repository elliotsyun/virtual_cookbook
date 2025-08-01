import { useState, useEffect } from 'react'
import './App.css'
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import { Layout } from './componenets/Layout';
import { Home } from './pages/Home';
import { AddRecipe } from './pages/AddRecipe';
import { EditRecipe } from './pages/EditRecipe';


function App() {

  const [recipes, setRecipes] = useState([]); 
  const [currentRecipe, setCurrentRecipe] = useState({})

  return (
    <>
      <Router>
        <Routes>
          <Route element={<Layout />}>
            <Route path="/" element={<Home recipes={recipes} setRecipes={setRecipes} currentRecipe={currentRecipe} setCurrentRecipe={setCurrentRecipe} />} />
            <Route path="/add_recipe" element={<AddRecipe/>}/>
            <Route path="/edit_recipe" element={<EditRecipe currentRecipe={currentRecipe} setCurrentRecipe={setCurrentRecipe}/>} />
          </Route>
        </Routes>
      </Router>
    </>
  );
}

export default App
