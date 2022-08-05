import React from 'react';
import { useNavigate,useParams } from 'react-router-dom';
import { APICall, fileToDataUrl } from '../helperFunc';
import NavigationBarHome from '../components/NavigationBarHome';
import styles from './styles/ModifyRecipe.module.css';
import IconButton from '@mui/material/IconButton';
import AddIcon from '@mui/icons-material/AddCircleOutlineSharp';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import CancelIcon from '@mui/icons-material/Cancel';
import SearchBarRecipe from '../components/SearchBarRecipe';
import SearchSkillAddBar from '../components/SearchSkillAddBar';
import Loading from '../components/Loading';

export default function ModifyRecipes () {
  const id = useParams();
  const navigate = useNavigate();
  const [ingredients, setIngredients] = React.useState([{}])
  const [steps, setSteps] = React.useState([{description: '', step_id: 0}])
  const [tags, setTags] = React.useState([])
  const [recipeVideos, setRecipeVideos] = React.useState([]);
  const [recipe, setRecipe] = React.useState({});
  const [selectedIngredients, setSelectedIngredients] = React.useState([{}]);
  const [checkState, setCheckState] = React.useState('');
  const is_contributor = localStorage.getItem('is_contributor');
  const [isContributor, setIsContributor] = React.useState('')
  const token = localStorage.getItem('token');
  const [loading, setLoading] = React.useState(true)
  
  /* For SearchBar */
	const [listIngredient, setListIngredient] = React.useState([]);
	const [listCategories, setListCategories] = React.useState([]);
  const [tagData, setTagData] = React.useState([]);
  const [skillVideos, setSkillVideos] = React.useState([]);
  
  const getSkillVideos = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      data = await APICall(null, `/skill_videos`, 'GET', headers);
      setSkillVideos(data.video_list);
    } catch (err) {
      alert(err);
    }
  }

  const checkIfContributor = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      data = await APICall(null, `/is_contributor`, 'GET', headers);
      setIsContributor(data.is_contributor)
    } catch (err) {
      alert(err);
    }
  }
  
  const getAllCategories = async() => {
		let data = []; let temp = [];
		try {
			const headers = {
			  'Content-Type': 'application/json',
			};
			data = await APICall(null, '/categories', 'GET', headers);
			for (let i = 0; i < data.body.categories.length; i++) {
				temp.push({"c_id": data.body.categories[i].c_id, "name": data.body.categories[i].name})
			}
			setListCategories(temp);
		} catch (err) {
			alert(err);
		}
	}
	
	const getAllIngredients = async() => {
		let data = []; let temp = [];
		try {
			const headers = {
				'Content-Type': 'application/json',
			};
			data = await APICall(null, `/ingredients?query= `, 'GET', headers);
			for (let i = 0; i < data.body.suggestions.length; i++) {
				temp.push({"ingredient_id": data.body.suggestions[i].i_id, "name": data.body.suggestions[i].name, "c_id": data.body.suggestions[i].c_id})
			}
			setListIngredient(temp);
		} catch (err) {
			alert(err);
		}
	}
  
  const getAllTags = async() => {
		let tag_cat_data = []; let tag_data =[]; let temp = [];
		try {
			const headers = {
			  'Content-Type': 'application/json',
			};
			tag_cat_data = await APICall(null, '/search/tag/categories', 'GET', headers);
      for (let i = 0; i < tag_cat_data.tag_categories.length; i++) {
        tag_data = await APICall(null, `/search/tag/tags?tag_category_id=${tag_cat_data.tag_categories[i].category_id}`, 'GET', headers);
        tag_cat_data.tag_categories[i]['tags'] = tag_data['tags']
      }
      setTagData(tag_cat_data.tag_categories)
		} catch (err) {
			alert(err);
		}
  }
  
  React.useEffect(() => { 
    if(!loading) {
      let isFetch = true;
      if(localStorage.getItem('token')) {
        checkIfContributor()
      }
      if (Object.keys(id).length !== 0) {
        getDetails();
      }
      getAllCategories();
      getAllIngredients();
      getAllTags();
      getSkillVideos();
      return () => isFetch = false;
    }
  }, [id, loading])
  
  const getDetails = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      const data = await APICall(null, `/recipe_details/view?id=${id.id}`, 'GET', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      setRecipe(data);
      setTags(data.tags);
      setIngredients(data.ingredients);
      setSelected(data.ingredients);
      setSteps(data.steps);
      setRecipeVideos(data.skill_videos);
      setCheckState(data.public_state)
      console.log(data)
    } catch (err) {
      alert(err);
    }
  }
  
  const setSelected = (data) => {
    let iUpdate = [];
    data.map((i, index) => {
      iUpdate = [...iUpdate, 
        {
          name: i.name,
          ingredient_id: i.ingredient_id, 
        }
      ]
    })
    setSelectedIngredients(iUpdate)
  }
  
  const handleIngredientsChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...ingredients];
    list[index][name] = value;
    setIngredients(list);
    setRecipe({...recipe, ingredients: list})
  };

  const handleIngredientsRemove = (e, index) => {
    e.preventDefault()
    const list = [...ingredients];
    list.splice(index, 1);
    setIngredients(list);
    setRecipe({...recipe, ingredients: list})
  };
  
  const handleIngredientsAdd = (e) => {
    e.preventDefault()
    setIngredients([...ingredients, { description: '', ingredient_id: -1, name: ''}]);
  };
  
  const handleUpdateIngredients = (index, dataChange) => {
    let iUpdate = [...ingredients]
    iUpdate[index] = dataChange
    setIngredients(iUpdate);
    setRecipe({...recipe, ingredients: iUpdate})
  }
  
  const handleStepsChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...steps];
    list[index][name] = value;
    setSteps(list);
    setRecipe({...recipe, steps: list})
  };

  const handleStepsRemove = (e, index) => {
    e.preventDefault()
    const list = [...steps];
    const deleted = list.splice(index, 1);
    const deleted_id = deleted[0].step_id
    const decrement = list.map(function(step) {
      if(step.step_id < deleted_id) {return step;}
      return {description: step.description, step_id: step.step_id-1};
    })
    setSteps(decrement);
    setRecipe({...recipe, steps: list})
  };

  const handleStepsAdd = (e) => {
    e.preventDefault()
    setSteps([...steps, { description: "" , step_id: steps.length}]);
  };
  
  const handleFoodPic = (e) => {
    const file = e.target.files[0];
    fileToDataUrl(file)
      .then((res) => {
        setRecipe({image: res});
      })
  }
  
  
  const handleChanges = (e) => {
    const {name, value} = e.target
    if (name === 'image') {
      const file = e.target.files[0];
      fileToDataUrl(file)
      .then((res) => {
          setRecipe({...recipe, [name]: res});
        })
      } else {
      setRecipe({...recipe, [name]: value})
    }
  }
  
  const handleSave = async (state) => {
    let pass_id;
    let ori_id;
    console.log(recipe.original_id)
    if((is_contributor === 'false' && checkState === 'public') ||     //user creating own copy of public recipe
      (is_contributor === 'true' && state === 'private' && checkState === 'public')){   //contributor editing private recipe thats never been published before
      console.log("HERE!")
      ori_id = parseInt(id.id);
      pass_id = -1
    } else if (Object.keys(id).length === 0) {
      console.log("NOWHERE!")
      pass_id = -1
      ori_id = null
      //ori_id = recipe.original_id
    } else {
      console.log("THERE!")
      ori_id = recipe.original_id
      pass_id = parseInt(id.id)
    }
    const ingredient = recipe.ingredients;
    const step = recipe.steps;
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      const requestBody = {
        recipe_id: pass_id,
        title: `${recipe.title}`,
        description: `${recipe.description}`,
        image: `${recipe.image}`,
        time_required: `${recipe.time_required}`,
        skill_videos : recipeVideos,
        servings: `${recipe.servings}`,
        ingredients: ingredient,
        tags: tags,
        steps: step,
        video: `${recipe.video}`,
        public_state: state,
        original_id: ori_id
      }
      console.log(requestBody)
      const data = await APICall(requestBody, `/recipe_details/update`, 'PUT', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      if(isContributor) {
        navigate('/contributorProfile')
      }
      else {
        navigate('/userProfile')
      }

    } catch (err) {
      alert(err);
    }
  }
  
  const checkTags = (object) => {
    if(tags.map(v=>v.tag_id).includes(object.tag_id)){
      return true
    }
    return false
  }
  
  const handleTagsChange = (e, object) => {
    if(e.target.checked) {
      setTags([...tags, object]);
    } else {
      setTags(curr =>
        curr.filter(tag => {
          return tag.tag_id !== object.tag_id
      }))
    }
  }
  
  const handleSkillVideoChange = (object, index) => {
    const list = [...recipeVideos];
    list[index] = object;
    setRecipeVideos(list)
  }
  
  const handleSkillVideoAdd = (e) => {
    e.preventDefault()
    setRecipeVideos([...recipeVideos, { title: '', url: '', video_id: -1}]);
  }
  
  const handleSkillVideoDelete = (e, index) => {
    e.preventDefault()
    const list = [...recipeVideos];
    list.splice(index, 1);
    setRecipeVideos(list);
  }

  
  return (
    <>
      {(loading) && <Loading close={() => {setLoading(false)}}></Loading>}
      {(!loading) &&<div className={styles.screen_container}>
        <NavigationBarHome style={{ alignSelf: 'start', position: 'absolute' }} isLogin={false}></NavigationBarHome>
        <div className={styles.form_container}>
          {Object.keys(id).length === 0 && <h2 className={styles.title}> Add New Recipe </h2>}
          {Object.keys(id).length !== 0 && <h2 className={styles.title}> Modify Recipe </h2>}
          <form className={styles.form_control}>
            <label for='dishName' >Dish Name: </label>
            <input name='title' id='dishName' type='text' value={recipe.title} onChange={(e) => handleChanges(e)}/>
            <label for='dishPic'> Upload Image: </label>
            <input name='image' type="file" id="dishPic" accept=".png,.jpeg,.jpg" onChange={(e) => handleChanges(e)} />
            <img src={recipe.image} className={styles.foodPic}/>
            <label for='video'>Video: </label>
            <input name='video' id='dish_video' type='text' value={recipe.video} onChange={(e) => handleChanges(e)}/>
            <label for='duration'>Duration: </label>
            <input name='time_required' id='duration' type='text' value={recipe.time_required} onChange={(e) => handleChanges(e)}/>
            <label for='serving'>Serving: </label>
            <input name='servings' id='serving' type='text' value={recipe.servings} onChange={(e) => handleChanges(e)}/>
            <label for='desc' >Descriptions: </label>
            <input name='description' id='desc' type='text' value={recipe.description} onChange={(e) => handleChanges(e)}/>
            <label> Ingredients: </label>
            {ingredients.map((ingredient, index) => (
              <>
              {listCategories.length !== 0 &&
                <div key={index}>
                  <SearchBarRecipe 
                    preFilled={selectedIngredients[index]}
                    updateIngredients={handleUpdateIngredients}
                    index={index}
                    listCategories={listCategories}
                    listIngredient={listIngredient}
                  ></SearchBarRecipe>
                  <input
                    name='description'
                    type="text"
                    onChange={(e) => handleIngredientsChange(e, index)}
                    value={ingredient.description}
                  />
                  <button
                  onClick={(e) => handleIngredientsRemove(e, index)}
                  className={styles.remove_button}
                  > Remove </button>
                </div>
              }
              </>
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
                  onChange={(e) => 
                    handleStepsChange(e, index)}
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
            <div className={styles.tag_container}>
              {tagData.map((tags, index) => (
                <div key={index} className={styles.tag_categories}>
                  <label> {tags.name} </label>
                  {tags.tags.map((tag, index) => (
                    <div> 
                      <input type='checkbox' 
                        name={tag.tag_id} 
                        value={tag.name} 
                        defaultChecked={checkTags(tag)}
                        onChange={(e) => handleTagsChange(e, tag)}
                        />
                      <label for={tag.tag_id}> {tag.name} </label> 
                    </div>
                  ))}
                </div>
              ))}
            </div>
            <label>Videos Skill: </label>
            <div>
                {recipeVideos.map((vid, index) => (
                <> 
                  <span className={styles.video_skill_container}>
                    <SearchSkillAddBar 
                      data={skillVideos} 
                      updateVideoSkill={handleSkillVideoChange}
                      index={index}
                      preFilled={vid}
                      handleDelete={handleSkillVideoDelete}
                      ></SearchSkillAddBar>
                  </span>
                  <div className={styles.video_skill}></div>
                </>
              ))}
            </div>
            <IconButton aria-label="add" sx={{ ml: '40%' , mr: '55%' }} onClick={handleSkillVideoAdd}>
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
                }}
              onClick={() => {
              if(isContributor) {
                navigate('/contributorProfile')
              }
              else {
                navigate('/userProfile')
              }}}
                >
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
              onClick={() => handleSave('private')}
              >
              Save
            </Button>
            {is_contributor === 'true' && 
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
                  onClick={() => handleSave('public')}>
                Publish
              </Button>
            }
          </div>
        </div>
      </div>}
    </>
  )
}
