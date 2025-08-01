import { useState } from "react";
import { useNavigate } from "react-router-dom";

export function EditRecipe({currentRecipe, setCurrentRecipe}) {
    const [title, setTitle] = useState(currentRecipe.title)
    const [steps, setSteps] = useState(currentRecipe.steps || [""])
    const [ingredients, setIngredients] = useState(currentRecipe.ingredients || [""])


    const navigate = useNavigate();

    // currently only for ingredients/steps, adding boxes
    const handleAddField = (stateVar, setter) => {
        const values = [...stateVar];
        values.push("")
        setter(values);
    };

    // when the input of a box is changed, add to the state variable array
    const handleInputChange = (index, event, stateVar, setter) => {
        const values = [...stateVar];
        values[index] = event.target.value;
        setter(values);
    };      

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            title,
            steps,
            ingredients,
        }
        const url = "http://127.0.0.1:5000/" + `update_recipe/${currentRecipe.id}`
        const options = {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
      
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            setCurrentRecipe("")
            navigate('/')
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="title">Title:</label>
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
            </div>
            
            { /* EDIT STEPS FIELDS -> in future these should be components */ }
            <div>               
                {steps.map((step, index) => (
                    <div key={index}>
                        <label  >Step {index + 1} </label>

                        <input
                            id={"step" + index} 
                            type="text"
                            value={step}    
                            onChange={(e) => handleInputChange(index, e, steps, setSteps)}
                        />
                    </div>
                ))}
            </div> 
            <button type="button" onClick={() => handleAddField(steps, setSteps)}>
                Add Step
            </button>   

            { /* EDIT INGREDIENT FIELDS -> in future these should be components */ }
            <div>               
                {ingredients.map((ingredient, index) => (
                    <div key={index}>
                        <label>Ingredient {index + 1} </label>

                        <input
                            id={"ingredient" + index}
                            type="text"
                            value={ingredient}
                            onChange={(e) => handleInputChange(index, e, ingredients, setIngredients)}
                        />
                    </div>
                ))}
            </div> 
            <button type="button" onClick={() => handleAddField(ingredients, setIngredients)}>
                Add Ingredient
            </button>               

            <button type="submit">Update</button>
        </form>
    )
}