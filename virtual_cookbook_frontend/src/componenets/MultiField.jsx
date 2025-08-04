

export function MultiField({stateVar, setter, fieldUnit}) {

    // currently only for ingredients/steps, adding boxes
    const handleAddField = (stateVar, setter) => {
        const values = [...stateVar];
        values.push("")
        setter(values);
    };

    // when the input of a box is changed, add to the state variable array
    const handleInputChange = (index, event, stateVar, setter) => {
        const values = [...stateVar];
        const updatedValue = event.target.name;
        values[index] = event.target.value;
        setter(values);
    };        

    return (
        <>
            <div>               
                {stateVar.map((unit, index) => (
                    <div key={index}>
                        <label  >{fieldUnit} {index + 1} </label>

                        <input
                            id={fieldUnit + index} 
                            type="text"
                            value={unit}    
                            onChange={(e) => handleInputChange(index, e, stateVar, setter)}
                        />
                    </div>
                ))}
            </div> 
            <button type="button" onClick={() => handleAddField(stateVar, setter)}>
                Add {fieldUnit}
            </button>   
        </>
    )
}