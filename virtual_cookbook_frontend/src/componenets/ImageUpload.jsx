

export function ImageUpload({setImageFile}) {

    return (
        <>
            <div>
                <label>Image:</label>
                
                { /* hidden input + label with the 'for' tag => not ugly upload button */ }
                <input
                    type="file"
                    accept="image/*"

                    // NOTE THAT THE "files[0]" means that only one file upload is supported currently
                    onChange={(e) => setImageFile(e.target.files[0])}
                    id="upload_button"
                hidden/>
                <label for="upload_button"> INPUT HERE! </label>
            </div>        
        
        </>
    )
}