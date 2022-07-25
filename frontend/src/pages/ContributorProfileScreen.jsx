import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import ContributorDashboard from '../components/ContributorDashboard';
import RecipeCard from '../components/RecipeCard';
import ContributorRecipeCard from '../components/ContributorRecipeCard'
import { APICall } from '../helperFunc';
import AddIcon from '@mui/icons-material/Add';
import Box from '@mui/material/Box';
import SpeedDial from '@mui/material/SpeedDial';
import SpeedDialIcon from '@mui/material/SpeedDialIcon';
import SpeedDialAction from '@mui/material/SpeedDialAction';
import RecipeImg from '../assets/recipe-book.png';
import VideoFileIcon from '@mui/icons-material/VideoFile';
import IngImg from '../assets/harvest.png'

export default function ContributorProfileScreen () {
  const navigate = useNavigate();
  const [tabValue, setTabValue] = React.useState("Published")
  const [publishedRecipes, setPublishedRecipes] = React.useState([])
  const [shownRecipes, setShownRecipes] = React.useState([])
  const [draftRecipes, setDraftRecipes] = React.useState([])
  const [ratedRecipes, setRatedRecipes] = React.useState([])
  const [statistic, setStatistic] = React.useState([])

  
  React.useEffect(() => {
    if (!localStorage.getItem('token')){
      alert("Please Log in Beforehand")
      navigate("/")
    }
    fetchStatistics()
  }, [])
  
  const fetchSaved = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/saved', 'GET', headers);
      let data = []
      for(let i = 0; i < temp_data.recipes.length; i++) {
        data.push({
          "recipe_id" : temp_data.recipes[i].recipe_id,
          "recipe_name": temp_data.recipes[i].title,
          "recipe_desc": temp_data.recipes[i].description,
          "recipe_time": temp_data.recipes[i].time_required,
          "is_liked": temp_data.recipes[i].saved,
          "recipe_ratings": temp_data.recipes[i].avg_rating,
          "recipe_tags": temp_data.recipes[i].tags,
          "recipe_image": temp_data.recipes[i].image
        })
      }
      setShownRecipes(data)
    } catch (err) {
      alert(err);
    }
  }
  
  const fetchMyRecipes = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/my_recipes', 'GET', headers);
      console.log("My reicpeeeee")
      console.log(temp_data)
      let data = []
      for(let i = 0; i < temp_data.recipes.length; i++) {
        data.push({
          "recipe_id" : temp_data.recipes[i].recipe_id,
          "recipe_name": temp_data.recipes[i].title,
          "recipe_desc": temp_data.recipes[i].description,
          "recipe_time": temp_data.recipes[i].time_required,
          "is_liked": temp_data.recipes[i].saved,
          "recipe_ratings": temp_data.recipes[i].avg_rating,
          "recipe_tags": temp_data.recipes[i].tags,
          "recipe_image": temp_data.recipes[i].image
        })
      }
      setDraftRecipes(data)
    } catch (err) {
      alert(err);
    }
  }
  
  const fetchStatistics = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/statistics', 'GET', headers);
      console.log("My reicpeeeee")
      console.log(temp_data)
      setStatistic(temp_data.statistics)
    } catch (err) {
      alert(err);
    }
  }
  
  const fetchRated = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/rated', 'GET', headers);
      setRatedRecipes(temp_data)
    } catch (err) {
      alert(err);
    }
  }
  
  const fetchPublishedRecipes = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/my_recipes', 'GET', headers);
      
      let data = []
      for(let i = 0; i < temp_data.recipes.length; i++) {
        data.push({
          "recipe_id" : temp_data.recipes[i].recipe_id,
          "recipe_name": temp_data.recipes[i].title,
          "recipe_desc": temp_data.recipes[i].description,
          "recipe_time": temp_data.recipes[i].time_required,
          "is_liked": temp_data.recipes[i].saved,
          "recipe_ratings": temp_data.recipes[i].avg_rating,
          "recipe_tags": temp_data.recipes[i].tags,
          "recipe_image": temp_data.recipes[i].image
        })
      }
      setPublishedRecipes(data)
    } catch (err) {
      alert(err);
    }
  }
  
  React.useEffect(() => {
    //Fetch the recipe
    if(tabValue === 'Saved') {
      fetchSaved()
    } else if (tabValue === 'Rated') {
      fetchRated()
    } else if (tabValue === 'Drafted') {
      fetchMyRecipes()
    } else if (tabValue === 'Published') {
      fetchPublishedRecipes()
    } else if (tabValue === 'Video') {
      // TODO
    }
  }, [tabValue])
  
  const renderRecipesCard = () => {
    let content = []
    let listRecipes = []
    let func = null
    if (tabValue === 'Saved') {
      listRecipes = shownRecipes
      func = fetchSaved
    }
    if (tabValue === 'Drafted') {
      listRecipes = draftRecipes
      func = fetchMyRecipes
    }
    for (let i = 0; i < listRecipes.length; i++) {
      content.push(
        <RecipeCard object={listRecipes[i]} isDelete={false} handleAfterLike={func}/>
        )
      }
      return content
    }
    
  const renderRatedRecipes = () => {
    let data = []
    for (const [key, value] of Object.entries(ratedRecipes)) {
      let content = []
      if (value.length === 0) break
      for (let j = 0; j < value.length; j++) {
        content.push(
          <RecipeCard object={{
            "recipe_id" : value[j].recipe_id,
            "recipe_name": value[j].title,
            "recipe_desc": value[j].description,
            "recipe_time": value[j].time_required,
            "is_liked": value[j].saved,
            "recipe_ratings": value[j].avg_rating,
            "recipe_tags": value[j].tags,
            "recipe_image": value[j].image
          }} isEditable={false} isDelete={false} handleAfterLike={fetchRated}/>
        )
      }
      let wrapper = (
        <div style= {{
          position: 'relative',
          display: 'flex',
          flexDirection: 'column',
          width: '100%',
          marginBottom: '20px' 
        }}>
          <div style={{
            fontSize: '25px',
            fontWeight: 'bold'
          }}>
            {key}
          </div>
          <div style={{
            position: 'relative',
            display: 'flex',
            flexDirection: 'row',
            justifyContent: 'space-evenly',
            alignItems: 'center',
            flexWrap: 'wrap',
            alignContent: 'center',
            width: '100%'
          }}> 
            {content}
          </div>
        </div>
      )
      data.push(wrapper)
    }
    return (
      <div style={{
        position: 'relative',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'flex-start',
        alignItems: 'flex-start',
        width: '90%',
        marginTop: '20px',
        marginLeft: '20px',
      }}>
        {data}
      </div>
    )
  }
  
  const renderContributorRecipesCard = () => {
    let content = []
    // if (publishedRecipes.length == statistic.length) {
    for (let i = 0; i < publishedRecipes.length; i++) {
      let index = 0
      for (let j = 0; j < statistic.length; j++) {
        if (statistic[j].recipe_id === publishedRecipes[i].recipe_id) index = j
      }
      content.push(
        <ContributorRecipeCard object={publishedRecipes[i]} isDelete={true} statistic={statistic[index]} afterDelete={handleAfterDelete} afterLike={handleAfterLike}/>
      )
    }
    return content
  }
      
  const handleAfterLike = async() => {
    await fetchStatistics()
    await fetchPublishedRecipes()
  }
      
  const handleAfterDelete = (recipe_id) => {
    const newStat = statistic.filter((recipeStat) => recipeStat.recipe_id !== recipe_id)
    setStatistic(newStat)
    const newPublRecipes = publishedRecipes.filter((recipe) => recipe.recipe_id !== recipe_id)
    setPublishedRecipes(newPublRecipes)
  }
      
  const style = {
    margin: 0,
    top: 'auto',
    right: 60,
    bottom: 40,
    left: 'auto',
    position: 'fixed',
  };
      
  const actions = [
    { icon: <img src={RecipeImg} style={{width: '45px', height: '45px'}} />, name: 'Add New Recipe', onClick: () => navigate(`/recipe/add`) },
    { icon: <img src={IngImg} style={{width: '45px', height: '45px'}} />, name: 'Add New Ingredient' },
    { icon: <VideoFileIcon sx={{width: '45px', height: '45px'}}/>, name: 'Add New Video' },
  ];


  return (
    <>
      <div style={{ 
        display:'flex',
        flexDirection:'column',
        height: '100%',
        alignItems:"center"
      }}>
        <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>

        <ContributorDashboard tabValue={tabValue} setTabValue={setTabValue}></ContributorDashboard>

        {(tabValue == 'Published') && <div style={{
          position: 'relative',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'flex-start',
          alignItems:'center',
          marginTop: '20px',
          marginLeft: '20px',
          width: '90%'
        }}>
          {renderContributorRecipesCard()}
          {/* <Fab color="primary" aria-label="add" size="large" style={style} onClick={()=>navigate(`/recipe/add`)}>
            <AddIcon />
          </Fab> */}
        </div>}
        {(tabValue == 'Saved' || tabValue == 'Drafted') && <div style={{
          position: 'relative',
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'space-evenly',
          flexWrap: 'wrap',
          alignContent: 'flex-start',
          marginTop: '20px',
          marginLeft: '20px',
          width: '90%'
        }}>
          {renderRecipesCard()}
        </div>}
        {(tabValue === "Rated") && renderRatedRecipes()}
      </div>
      <Box style={style} sx={{ height: 320, transform: 'translateZ(0px)', flexGrow: 1 }}>
        <SpeedDial
          ariaLabel="SpeedDial basic example"
          sx={{ position: 'absolute', bottom: 16, right: 16, '& .MuiFab-primary': { width: 80, height: 80 } }}
          icon={<SpeedDialIcon />}
          >
          {actions.map((action) => (
            <SpeedDialAction
            sx={{ width: 68, height: 68, '& .MuiSpeedDialAction-staticTooltipLabel': { width: 180, height: 40, backgroundColor: "red", fontSize: '0.9em' } }}
            key={action.name}
            icon={action.icon}
            tooltipTitle={action.name}
            onClick={action.onClick}
            // tooltipOpen
            />
            ))}
        </SpeedDial>
      </Box>
    </>
  )
}