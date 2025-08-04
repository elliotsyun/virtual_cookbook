import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { MultiField } from "../componenets/MultiField";

export function AddRecipe () {
    const [title, setTitle] = useState("");
    const [steps, setSteps] = useState([""]);
    const [ingredients, setIngredients] = useState([""]);
    const [tags, setTags] = useState([""]);
    

    const navigate = useNavigate();

    // logic for submitting a POST request
    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            title,
            steps,
            ingredients,
            tags,
        }
        const url = "http://127.0.0.1:5000/" + "create_recipe"
        const options = {
            method: "POST",
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
            navigate("/")
        }
    }

    return (
        <form onSubmit={onSubmit}>
            
            { /* ADD TITLE FIELD */ }
            <div>
                <label>Title:</label>
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
            </div>
            
            { /* Fields for adding multiple ingredients/steps */ }
            <MultiField stateVar={steps} setter={setSteps} fieldUnit={"Step"}/>
            
            <MultiField stateVar={ingredients} setter={setIngredients} fieldUnit={"Ingredient"}/>
            
            { /* SUBMIT BUTTON */ }
            <div>
                <button onClick={(e) => onSubmit(e)}>Create</button>            
            </div>                     
        </form>
    );
}