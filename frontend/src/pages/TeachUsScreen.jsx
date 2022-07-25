import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import VideoCard from '../components/VideoCard';
import VideoFrame from '../components/VideoFrame';
import VideoSearchBar from '../components/VideoSearchBar';

export default function TeachUsScreen () {
  const dummyVid = [
    "https://www.youtube.com/watch?v=LB9KDxAOMvI",
    "https://www.youtube.com/watch?v=a-2n_g4AdDM",
    "https://www.youtube.com/watch?v=tpikKCfm-kU&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=3",
    "https://www.youtube.com/watch?v=XhRIqzUDqAM&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=4",
    "https://www.youtube.com/watch?v=2ZxMNXBwHfQ&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=5",
    "https://www.youtube.com/watch?v=ie6GyJbtDP8&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=6",

    "https://www.youtube.com/watch?v=LB9KDxAOMvI",
    "https://www.youtube.com/watch?v=a-2n_g4AdDM",
    "https://www.youtube.com/watch?v=tpikKCfm-kU&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=3",
    "https://www.youtube.com/watch?v=XhRIqzUDqAM&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=4",
    "https://www.youtube.com/watch?v=2ZxMNXBwHfQ&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=5",
    "https://www.youtube.com/watch?v=ie6GyJbtDP8&list=PLTzMGnJjrsSy6H8uiX3XKWtUhhj2Vilw1&index=6",
  ]

  const navigate = useNavigate();

  const [searchedTitle, setSearchedTitle] = React.useState("")
  const [open, setOpen] = React.useState(false);
  const [selectedVideo, setSelectedVideo] = React.useState('')
  const handleClickOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  const handleClickVideoCard = (url) => {
    setSelectedVideo(url)
    handleClickOpen()
  }
  const handleCloseVideoCard = () => {
    setSelectedVideo('')
    handleClose()
  }
  const renderVideoCard = () => {
    let content = []
    for (let i = 0; i < dummyVid.length; i++) {
      content.push(
        <VideoCard url={dummyVid[i]} onClick={handleClickVideoCard}/>
      )
    }
    return content
  }


  return (
  <div>
    <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
    <div style={{display:'flex', flexDirection:'column', justifyContent:'center', alignItems:'center'}}>
      <VideoSearchBar wordEntered={searchedTitle} setWordEntered={setSearchedTitle}></VideoSearchBar>
      <div style={{
        position: 'relative',
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-evenly',
        flexWrap: 'wrap',
        alignContent: 'flex-start',
        marginTop: '20px',
        marginLeft: '20px',
      }}>
        {renderVideoCard()}
      </div>
    </div>
    <VideoFrame openState={open} url={selectedVideo} handleClose={handleCloseVideoCard} handleClickOpen={handleClickOpen}></VideoFrame>
  </div>
  )
}