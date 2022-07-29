import React from 'react';
import { APICall } from '../helperFunc';
import Pagination from '@mui/material/Pagination';
import NavigationBarHome from '../components/NavigationBarHome';
import VideoCard from '../components/VideoCard';
import VideoSearchBar from '../components/VideoSearchBar';

export default function TeachUsScreen () {

  const [skillVideos, setSkillVideos] = React.useState([])
  const [isContributor, setIsContributor] = React.useState('')
  const [foundVideos, setFoundVideos] = React.useState([])
  const [currentPage, setCurrentPage] = React.useState(-1)
  const [maxPage, setMaxPage] = React.useState(-1)

  const handleChange = (event, value) => {
    setCurrentPage(value);
  };

  const getSkillVideos = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
      };
      data = await APICall(null, `/skill_videos`, 'GET', headers);
      setSkillVideos(data.video_list);
      setFoundVideos(data.video_list)
      setMaxPage(Math.ceil(data.video_list.length / 9))
      setCurrentPage(1)
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

  React.useEffect(() => {
    getSkillVideos()
    checkIfContributor()
  },[])

  const [searchedTitle, setSearchedTitle] = React.useState("")

  React.useEffect(() => {
    let temp;
    if (searchedTitle !== '') {
      temp = skillVideos.filter((video) => {
        if (video.title.toLowerCase().includes(searchedTitle.toLowerCase())) return video
      })
      setFoundVideos(temp)
    } else {
      temp = skillVideos
      setFoundVideos(temp)
    }
    setMaxPage(Math.ceil(temp.length / 9))
  }, [searchedTitle])
  
  React.useEffect(() => {
    setCurrentPage(1)
  },[foundVideos])


  const renderVideoCard = () => {
    let content = []
    if (foundVideos.length !== 0) {
      let index = (currentPage - 1 ) * 9
      let times = 9
      if (currentPage === maxPage) times = foundVideos.length % 9
      if (times === 0) times = 9
      for (let i = 0; i < times; i++) {
        content.push(
          <VideoCard url={foundVideos[index]['url']} object={foundVideos[index]} isContributor={isContributor}/>
        )
        index++;
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
  <div>
    <NavigationBarHome style={{ alignSelf: 'start' }} ></NavigationBarHome>
    <div style={{display:'flex', flexDirection:'column', justifyContent:'center', alignItems:'center'}}>
      <VideoSearchBar wordEntered={searchedTitle} setWordEntered={setSearchedTitle}></VideoSearchBar>
      {renderVideoCard()}
    </div>
  </div>
  )
}