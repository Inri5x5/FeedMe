import React from 'react'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { APICall } from '../helperFunc';
import { IconButton, CardActionArea, CardActions } from '@mui/material';
import VisibilityIcon from '@mui/icons-material/Visibility';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import FavoriteIcon from '@mui/icons-material/Favorite';
import DeleteIcon from '@mui/icons-material/Delete';
import Avatar from '@mui/material/Avatar';
import styles from './styles/VideoCard.module.css'
import VideoFrame from './VideoFrame';

const VideoCard = (props) => {
  const getYouTubeId = require('get-youtube-id')
  // Erivan's test email credentials
  // const API_Key = 'AIzaSyB7_DOdz0dsKg1OX52J_URhxapYF05DUwg'
  const API_Key = 'AIzaSyC2_FbK76-gw9IAHVu7h4DK-zSSO3CetZg'
  
  const [url, setUrl] = React.useState('')
  const [videoData, setVideoData] = React.useState({
    title : '',
    thumbnail: {url : ''},
    viewCount: -1,
    likeCount: -1,
    url: '',
    y_id: '',
  })

  const [selectedVideo, setSelectedVideo] = React.useState(props.url)
  const [open, setOpen] = React.useState(false);
  const handleClickOpen = () => {
    setOpen(true);
    setSelectedVideo(props.url)
  };
  const handleClose = () => {
    setSelectedVideo('')
    setOpen(false);
  };

  React.useEffect(() => {
    const vid = props.url
    setUrl(vid)
  })

  React.useEffect(() => {
    if(url !== '') {
      const id = getYouTubeId(url)
      fecthYoutubeMeta(id, url)
    }
  },[url])

  const convert = (value) => {
    if (value >= 1000000) {
      value=((value/1000000).toFixed(1))+"M"
    }
    else if (value >= 1000) {
      value=((value/1000).toFixed(1))+"K";
    }
    return value;
  }

  const fecthYoutubeMeta = async(y_id, url) => {
    let data = []; let temp = {};
    try {
        const headers = {
          'Content-Type': 'application/json',
        };
        data = await APICall(null, `https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=${y_id}&key=${API_Key}`, 'GET', headers);
        temp['title'] = data['items'][0]['snippet']['title']
        temp['thumbnail'] = data['items'][0]['snippet']['thumbnails']['high']
        temp['viewCount'] = data['items'][0]['statistics']['viewCount']
        temp['likeCount'] = data['items'][0]['statistics']['likeCount']
        temp['url'] = url
        temp['y_id'] = y_id
        setVideoData(temp)
    } catch (err) {
        alert(err);
    }
  }

  const deleteVideo = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "video_id" : props.object.id
      }
      await APICall(requestBody, '/skill_videos/delete', 'DELETE', headers);
      props.afterDelete(props.object.id)
    } catch (err) {
      alert(err);
    }
  }

  const saveVideo = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "video_id" : props.object.id
      }
      await APICall(requestBody, '/skill_videos/save', 'POST', headers);
      if (props.handleAfterLike) props.handleAfterLike(props.object.id)
    } catch (err) {
      alert(err);
    }
  }
  
  
  return (
    <>
      <Card sx={{ 
          width: '430px',
          height: '390px', 
          m: 2, 
          boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", 
          borderRadius: '0', 
          position: 'relative',
          transition: 'transform .2s',
          '&:hover': {
              transform : 'scale(1.1)'
          }
      }}>
        <CardActionArea onClick={()=> handleClickOpen()}>
          <CardMedia
            component="img"
            image={videoData['thumbnail']['url']}
            alt="green iguana"
            sx={{
              width: '100%',
              aspectRatio: '16/9'
            }}
          />
          <CardContent sx={{paddingBottom: 0}}>
            <div style={{display:'flex'}}>
              <Avatar alt="Travis Howard" src={props.object.creator_profile_pic} />
              <div className={styles.text_container}>
                {props.object.title}
              </div>
            </div>
            <div style={{marginTop: '10px'}}> {props.object.creator}</div>
          </CardContent>
        </CardActionArea>

        <CardActions sx={{
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'space-between'
        }}>
          <div style={{
              display:'flex',
              flexDirection:'row',
            }}>
            <div style={{
              display:'flex',
              flexDirection:'row',
              alignItems:'center',
              marginLeft: '10px',
            }}> 
              <VisibilityIcon sx={{color:'orangered'}}></VisibilityIcon>
              <span style={{paddingTop:'2px', marginLeft:'10px'}}>{convert(videoData.viewCount)}</span>
            </div>
            <div style={{
              display:'flex',
              flexDirection:'row',
              alignItems:'center',
              marginLeft: '15px',
            }}> 
              <ThumbUpIcon sx={{color:'blue'}}></ThumbUpIcon>
              <span style={{paddingTop:'2px', marginLeft:'10px'}}>{convert(videoData.likeCount)}</span>
            </div>
          </div>
          
          {(props.isContributor !== false) && <IconButton aria-label="add to favorites" disabled={!localStorage.getItem('token')} onClick={() => saveVideo()} sx={{marginRight: '10px'}}>
            <FavoriteIcon />
          </IconButton>}
          {(props.isDeleteable) && <IconButton aria-label="add to favorites" disabled={!localStorage.getItem('token')} onClick={() => deleteVideo()} sx={{marginRight: '10px'}}>
            <DeleteIcon />
          </IconButton>}
        </CardActions>
      </Card>
      <VideoFrame openState={open} url={selectedVideo} handleClose={handleClose} handleClickOpen={handleClickOpen}></VideoFrame>
    </>
  )
}

export default VideoCard