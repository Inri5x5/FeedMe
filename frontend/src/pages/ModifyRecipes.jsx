import React from 'react';
import { useNavigate } from 'react-router-dom';
import { APICall, fileToDataUrl } from '../helperFunc';
import NavigationBarHome from '../components/NavigationBarHome';
import styles from './styles/ModifyRecipe.module.css';
import IconButton from '@mui/material/IconButton';
import AddIcon from '@mui/icons-material/AddCircleOutlineSharp';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import CancelIcon from '@mui/icons-material/Cancel';

export default function ModifyRecipes () {
  const navigate = useNavigate();
  const [foodPic, setFoodPic] = React.useState()
  const [ingredients, setIngredients] = React.useState([{ ingredients: "" }])
  const [steps, setSteps] = React.useState([{ steps: "" }])
  const [tags, setTags] = React.useState([{ tags: "" }])
  const is_contributor = localStorage.getItem('is_contributor');
  // const token = localStorage.get
  
  // const logginOut = async () => {
  //   try {
  //     const headers = {
  //       'Content-Type': 'application/json',
  //     };
  //     const requestBody = {
  //       token: token,
  //     };
  //     const data = await APICall(requestBody, `/logout`, 'POST', headers);
  //     if (data.error) {
  //       throw new Error(data.error);
  //     }
  //     localStorage.clear();
  //     navigate('/')
  //   } catch (err) {
  //     alert(err);
  //     navigate('/');
  //   }
  // }
  
  const handleIngredientsChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...ingredients];
    list[index][name] = value;
    setIngredients(list);
    console.log(list);
  };

  const handleIngredientsRemove = (e, index) => {
    e.preventDefault()
    const list = [...ingredients];
    list.splice(index, 1);
    setIngredients(list);
  };

  const handleIngredientsAdd = (e) => {
    e.preventDefault()
    setIngredients([...ingredients, { ingredients: "" }]);
  };
  
  const handleStepsChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...steps];
    list[index][name] = value;
    setSteps(list);
  };

  const handleStepsRemove = (e, index) => {
    e.preventDefault()
    const list = [...steps];
    list.splice(index, 1);
    setSteps(list);
  };

  const handleStepsAdd = (e) => {
    e.preventDefault()
    setSteps([...steps, { steps: "" }]);
  };
  
  const handleTagsChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...tags];
    list[index][name] = value;
    setTags(list);
  };

  const handleTagsRemove = (e, index) => {
    e.preventDefault()
    const list = [...tags];
    list.splice(index, 1);
    setTags(list);
  };

  const handleTagsAdd = (e) => {
    e.preventDefault()
    setTags([...tags, { tags: "" }]);
  };
  
  const handleFoodPic = (e) => {
    const file = e.target.files[0];
    fileToDataUrl(file)
      .then((res) => {
        setFoodPic(res);
      })
  }
  
  return (
  <div className={styles.screen_container}>
    <NavigationBarHome style={{ alignSelf: 'start', position: 'absolute' }} isLogin={false}></NavigationBarHome>
    <div className={styles.form_container}>
      <h2 className={styles.title}> Modify Recipe </h2>
      <form className={styles.form_control}>
        <label for='dishName' >Dish Name: </label>
        <input id='dishName' type='text'/>
        <label for='dishPic'> Upload Image: </label>
        <input type="file" id="dishPic" name="questionImage" accept=".png,.jpeg,.jpg" onChange={handleFoodPic} />
        {foodPic !== undefined && <img src={foodPic} className={styles.foodPic}/>}
        <label for='duration'>Duration: </label>
        <input id='duration' type='text'/>
        <label for='serving'>Serving: </label>
        <input id='serving' type='text'/>
        <label for='desc' >Descriptions: </label>
        <input id='desc' type='text'/>
        <div> 
          <label>Measurement: </label>
          <label className={styles.ingredients_label}> Ingredients: </label>
        </div>
        {ingredients.map((ingredient, index) => (
          <div key={index}>
            <input
              name='measurement'
              type="text"
              // onChange={(e) => handleIngredientsChange(e, index)}
              // value={ingredient.ingredients}
              className={styles.measurement_input}
            />
            <input
              name='ingredients'
              type="text"
              onChange={(e) => handleIngredientsChange(e, index)}
              value={ingredient.ingredients}
              className={styles.ingredients_input}
            />
            <button
            onClick={(e) => handleIngredientsRemove(e, index)}
            className={styles.remove_button}
            > Remove </button>
          </div>
        ))}
        <IconButton aria-label="add" sx={{ ml: '40%' , mr: '55%' }} onClick={handleIngredientsAdd}>
          <AddIcon />
        </IconButton>
        <label>Instructions: </label>
        {steps.map((step, index) => (
          <div key={index}>
            <input
              name='steps'
              type="text"
              onChange={(e) => handleStepsChange(e, index)}
              value={step.steps}
              />
            <button onClick={(e) => handleStepsRemove(e, index)}
            className={styles.remove_button}
            > Remove </button>
          </div>
        ))}
        <IconButton aria-label="add" sx={{ ml: '40%' , mr: '55%' }} onClick={handleStepsAdd}>
          <AddIcon />
        </IconButton>
        <label>Categories: </label>
        {tags.map((tag, index) => (
          <div key={index}>
            <input
              name='tags'
              type="text"
              onChange={(e) => handleTagsChange(e, index)}
              value={tag.tags}
              />
            <button onClick={(e) => handleTagsRemove(e, index)}
            className={styles.remove_button}
            > Remove </button>
          </div>
        ))}
        <IconButton aria-label="add" sx={{ ml: '40%' , mr: '55%' }} onClick={handleTagsAdd}>
          <AddIcon />
        </IconButton>
      </form>
      <div className={styles.button_container}>
        <Button variant="contained" endIcon={<CancelIcon />} 
          sx={{ 
            ml: '60%', 
            mb: '2%', 
            backgroundColor: '#F9D371', 
            color: '#F47340',
            fontFamily: "'Righteous', serif",
            '&:hover' : {
              backgroundColor: '#F47340',
              color: '#F9D371'
            }
            }}>
          Cancel
        </Button>
        <Button variant="contained" endIcon={<SendIcon />} 
          sx={{ 
            ml: '5%', 
            mb: '2%', 
            backgroundColor: '#F9D371', 
            color: '#F47340',
            fontFamily: "'Righteous', serif",
            '&:hover' : {
              backgroundColor: '#F47340',
              color: '#F9D371'
            }
            }}>
          Save
        </Button>
        <Button variant="contained" endIcon={<SendIcon />} 
          sx={{ 
            ml: '5%', 
            mb: '2%', 
            backgroundColor: '#F9D371', 
            color: '#F47340',
            fontFamily: "'Righteous', serif",
            '&:hover' : {
              backgroundColor: '#F47340',
              color: '#F9D371'
            }
            }}>
          Publish
        </Button>
      </div>
    </div>
  </div>
  )
}
