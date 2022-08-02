import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import UserDashboard from '../components/UserDashboard';
import RecipeCard from '../components/RecipeCard';
import VideoCard from '../components/VideoCard';
import Pagination from '@mui/material/Pagination';
import Loading from '../components/Loading';

import { APICall } from '../helperFunc';

export default function UserProfileScreen2 () {
  const navigate = useNavigate();

  const [tabValue, setTabValue] = React.useState("")
  const [shownRecipes, setShownRecipes] = React.useState([])
  const [ratedRecipes, setRatedRecipes] = React.useState([])
  const [myRecipes, setMyRecipes] = React.useState([])
  const [loading, setLoading] = React.useState(true)

  const [publishedVideos, setPublishedVideos] = React.useState([])
  const [currentPage, setCurrentPage] = React.useState(-1)
  const [maxPage, setMaxPage] = React.useState(-1)
  const handleChange = (event, value) => {
    setCurrentPage(value);
  };


  React.useEffect(() => {
    if (!loading) {
      if (!localStorage.getItem('token')){
        alert("Please Log in Beforehand")
        navigate("/")
      }
      setTabValue("Saved")
    }
  }, [loading])

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
      setMyRecipes(data)
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

  const fetchVideos = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/skill_videos/ruser', 'GET', headers);
      setPublishedVideos(temp_data.video_list)
      setMaxPage(Math.ceil(temp_data.video_list.length / 9))
      setCurrentPage(1)
    } catch (err) {
      alert(err);
    }
  }

  const handleAfterLike = (video_id) => {
    const newPublVideos = publishedVideos.filter((video) => video.id !== video_id)
    setMaxPage(Math.ceil(newPublVideos.length / 9))
    if ((Math.ceil(newPublVideos.length / 9)) < currentPage ) {
      setCurrentPage(Math.ceil(newPublVideos.length / 9))
    }
    setPublishedVideos(newPublVideos)
  }
  
  React.useEffect(() => {
    if(tabValue === 'Saved') {
      fetchSaved()
    } else if (tabValue === 'Rated') {
      fetchRated()
    } else if (tabValue === 'Own') {
      fetchMyRecipes()
    } else if (tabValue === 'Video') {
      fetchVideos()
    }
  }, [tabValue])

  const renderRecipesCard = () => {
    let content = []
    for (let i = 0; i < shownRecipes.length; i++) {
      content.push(
        <RecipeCard object={shownRecipes[i]} isEditable={false} isDelete={false} handleAfterLike={fetchSaved}/>
      )
    }
    return content
  }

  const renderMyRecipes = () => {
    let content = []
    for (let i = 0; i < myRecipes.length; i++) {
      content.push(
        <RecipeCard object={myRecipes[i]} isEditable={false} isDraft={false} isDelete={false} handleAfterLike={fetchMyRecipes}/>
      )
    }
    return content
  }

  const renderRatedRecipes = () => {
    let data = []
    for (const [key, value] of Object.entries(ratedRecipes)) {
      let content = []
      if (value.length === 0) continue
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


  const renderVideoCard = () => {
    let content = []
    if (publishedVideos.length !== 0) {
      let index = (currentPage - 1 ) * 9
      let times = 9
      if (currentPage === maxPage) times = publishedVideos.length % 9
      if (times === 0) times = 9
      for (let i = 0; i < times; i++) {
        content.push(
          <VideoCard url={publishedVideos[index]['url']} object={publishedVideos[index]} isContributor={false} isSaved={true} handleAfterLike={handleAfterLike}/>
        )
        index++
      }
      return (
        <div style={{width: '100%', display:'flex', flexDirection:'column', justifyContent:'center', alignItems:'center'}}>
          <div style={{
            width: '95%',
            display: 'flex',
            flexDirection: 'row',
            flexWrap: 'wrap',
            justifyContent: 'space-evenly',
            alignContent: 'space-between',
            marginTop: '20px',
          }}>
            {content}
          </div>
          <Pagination count={maxPage} page={currentPage} onChange={handleChange} size="large" color='primary' sx={{paddingBottom: 5, paddingTop: 5}}/>
        </div>
      )
    }
  }
  
  return (
    <>
      {(loading) && <Loading close={() => {setLoading(false)}}></Loading>}

      {(!loading) && <div style={{ 
        display:'flex',
        flexDirection:'column',
        height: '100%',
        alignItems:"center"
      }}>
        <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
        <UserDashboard tabValue={tabValue} setTabValue={setTabValue}></UserDashboard>
        {(tabValue === 'Saved') && <div style={{
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
        {(tabValue === "Own") && <div style={{
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
          {renderMyRecipes()}
        </div>}
        {(tabValue === 'Video') && renderVideoCard()}
      </div>}
    </>
  )
}