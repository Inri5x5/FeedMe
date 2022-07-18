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
import SearchBarRecipe from '../components/SearchBarRecipe';

export default function ModifyRecipes () {
  const navigate = useNavigate();
  const [ingredients, setIngredients] = React.useState([{ ingredients: "" }])
  const [steps, setSteps] = React.useState([{ steps: "" }])
  const [tags, setTags] = React.useState([{ tags: "" }])
  const [recipe, setRecipe] = React.useState({});
  const [selectedIngredients, setSelectedIngredients] = React.useState([{}]);
  const is_contributor = localStorage.getItem('is_contributor');
  const token = localStorage.getItem('token');
  const id = 0;
  
  React.useEffect(() => { 
    let isFetch = true;
    getDetails();
    return () => isFetch = false;
  }, [id])
  
  const getDetails = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      const data = await APICall(null, `/recipe_details/view?id=${id}`, 'GET', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      console.log(data);
      setRecipe(data);
      setTags(data.tags);
      setIngredients(data.ingredients);
      setSelected(data.ingredients);
      setSteps(data.steps);
    } catch (err) {
      alert(err);
    }
  }
  
  const setSelected = (data) => {
    let iUpdate = [];
    data.map((i, index) => {
      iUpdate = [...iUpdate, 
        {
          u_id: i.ingredient_id, 
          name: i.name
        }
      ]
    })
    setSelectedIngredients(iUpdate)
  }
  
  const handleIngredientsChange = (e, index) => {
    const { name, value } = e.target;
    console.log(e.target)
    const list = [...ingredients];
    list[index][name] = value;
    setIngredients(list);
    setSelected(list);
  };

  const handleIngredientsRemove = (e, index) => {
    e.preventDefault()
    const list = [...ingredients];
    list.splice(index, 1);
    setIngredients(list);
    setSelected(list);
  };

  const handleIngredientsAdd = (e) => {
    e.preventDefault()
    setIngredients([...ingredients, { decription: '', ingredient_id: -1, name: ''}]);
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
    setSteps([...steps, { description: "" , step_id: steps.length}]);
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
        setRecipe({image: res});
      })
  }
  
  const handleUpdateIngredients = (index, dataChange) => {
    let iUpdate = [...ingredients]
    iUpdate[index] = dataChange
    setIngredients(iUpdate);
    setSelected(ingredients);
  }
  
  const handleSave = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      const requestBody = {
        recipe_id: `${recipe.id}`,
        title: `${recipe.title}`,
        description: `${recipe.description}`,
        image: `${recipe.image}`,
        time_required: `${recipe.time_required}`,
        servings: `${recipe.servings}`,
        public_state: 'private'
      }
      const data = await APICall(requestBody, `/recipe_details/update`, 'PUT', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      console.log(data);
    } catch (err) {
      alert(err);
    }
  }
  console.log(steps)
  // console.log(ingredients)
  // console.log(selectedIngredients)
  // console.log(tags)
  return (
  <div className={styles.screen_container}>
    <NavigationBarHome style={{ alignSelf: 'start', position: 'absolute' }} isLogin={false}></NavigationBarHome>
    <div className={styles.form_container}>
      <h2 className={styles.title}> Modify Recipe </h2>
      <form className={styles.form_control}>
        <label for='dishName' >Dish Name: </label>
        <input id='dishName' type='text' value={recipe.title} onChange={(e) => setRecipe({title: e.target.value})}/>
        <label for='dishPic'> Upload Image: </label>
        <input type="file" id="dishPic" name="questionImage" accept=".png,.jpeg,.jpg" onChange={handleFoodPic} />
        <img src={recipe.image} className={styles.foodPic}/>
        <label for='duration'>Duration: </label>
        <input id='duration' type='text' value={recipe.time_required} onChange={(e) => setRecipe({time_required: e.target.value})}/>
        <label for='serving'>Serving: </label>
        <input id='serving' type='text' value={recipe.servings} onChange={(e) => setRecipe({servings: e.target.value})}/>
        <label for='desc' >Descriptions: </label>
        <input id='desc' type='text' value={recipe.description} onChange={(e) => setRecipe({description: e.target.value})}/>
        <label> Ingredients: </label>
        {ingredients.map((ingredient, index) => (
          <div key={index}>
            <SearchBarRecipe 
              preFilled={selectedIngredients[index]}
              updateIngredients={handleUpdateIngredients}
              index={index}
            ></SearchBarRecipe>
            <input
              name='decription'
              type="text"
              onChange={(e) => handleIngredientsChange(e, index)}
              value={ingredient.decription}
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
            <textarea
              name='description'
              type="text"
              onChange={(e) => handleStepsChange(e, index)}
              value={step.description}
              wrap= "soft"
              rows= "3"
              cols="104"
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
              value={tag.name}
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
            }}
          onClick={
            handleSave
          }
          >
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
