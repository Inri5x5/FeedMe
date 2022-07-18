import React from 'react';

import SearchBar from '../components/SearchBar';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterContainer from '../components/FilterContainer';
import RecipeCard from '../components/RecipeCard';
import { APICall } from '../helperFunc';
import { fontSize, fontWeight } from '@mui/system';


const HomeScreen = () => {
    const [selectedIngredients, setSelectedIngredients] = React.useState([]);
    const [selectedTags, setSelectedTags] = React.useState([]);
    const [foundRecipes, setFoundRecipes] = React.useState([]);

    //Dummy Recipes Set Up
    let dummyRecipes = [
      {
        "recipe_id" : 1,
        "recipe_name": 'Boiled Egg',
        "recipe_desc": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis amet odio dolorem nulla dolore hic enim blanditiis aperiam repellendus. Cum doloribus expedita ullam assumenda commodi molestias magnam est fugiat modi!",
        "recipe_time": 20,
        "is_liked": false,
        "recipe_ratings": 3.5,
        "recipe_tags": [{"tag_id" : 1, "tag_name" : "Australian"}],
        "recipe_image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTEhMVFhUXGBoYGBgXGRcXHRgXFxYXFxcYGhcYHSggGBolGxcXITEhJSkrLi4uFx8zODUtNygtLisBCgoKDg0OGxAQGy0mICUvLS0tLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAFAgMEBgcAAQj/xABIEAACAAMFBAYIAwYEBQQDAAABAgADEQQFEiExBkFRYRMicYGRoQcyQlKxwdHwI2JyFDNTgpLhFaKy8RY0Q3OTJGOjwxc1VP/EABsBAAIDAQEBAAAAAAAAAAAAAAUGAgMEAQAH/8QAOREAAQIEAwUHAwMDBAMAAAAAAQACAwQRIRIxQQVRcYHwEyJhkaGxwTLR4RQzUhUj8QZCcqIWNJL/2gAMAwEAAhEDEQA/AHdsdsEsidHLo045ADOlTlXx0+WuWWpmdjOtLVbWhNQO3ieQhcw4cU2a2KYTrrmdy8TzgXPYv15mS+yo38h8zFpeKYIdm+p4/ZVhpJxPz9B4Dq6VPtTTK06qbyfn9BDGOgovVHvH1j2cBHkxyaCmmijRe3iYQxprmfh98I8FIpYoBwHmY9lv7oAHvN8vswhJROZhyqrrmeAiwA8AoE80tNcgXbi3yX6w+6/xZn8oz8hkIZlmY+SDCOXzMTpF1UzIqYuYBoFBzqZ9c0wloA/dy+9sz9ItXo/2ae32is4n9nlUMymWI+zLHbv4DtEV+TZGeYsuWtXdgqgb2Y0A8Y3m6LPKu+VKsqDE2HE7D2phzZjvzOQ4ACKp6bbLQi9x669Klel4BjPoAic/DLCigVahVAyAyyAG4ACEzmoDhBJqABxqaViJ0TTJhmTMpaepXKtfa7MojTr9OJhJlljoGOgpwHbCfG2pEeTQ0HhnTn17I6yTaNK+ymNb1VsDkB+Fa07eESpIBzio2CwM0zExJJ1J5xZBO6NlQ6MMj+Yf2zjVI7UMR/ZxOR8dAfx5KmYlA0VYn2SME2+uMSLfMVRRJlJq5AABiagAbgwbyj6BURmXpdu0tNshQVeZikjmWZMA46sfGDoNKIfRUnZLZGZbZ+BGwylAaZM91ToBxY0NByJ3RtdwbN2WxgmzocRFC7ks3ifVryAhy5rkSxWSXZkoW/6j6Y3pVnPLKg4ADhE5moK6DKAe09qvBMGEaAZka7+Q1W+WlQRjcOC8WfgxdIRhNKHeK/KIdtm46LTEGPWLZjDwz1yhP7LjFZrHXJdKcKneaQ9a5WHAPezHdSkABNzbBjDzvrU5Lf2MI92g8ljm32yhs81ptmU9FTEyjROJX8ueY9mvDSr2e3VFHAI84+g7xkDocWGuEsTXOqn1geIIjCdrLoFktTywCJbUeUxzqjaZ76Gq90PGxtqOjwquNxSvO4PxxBQSclmtdlZMGy1FUNRwOohCTadVhUcDqIblOVoQYmqyzMmybcYZmUddtkMdVudx6qPgK5p1l3jhDkqZvQ90IZWlt90ML6PF1kyO9eMcwkZZ7lw0IqfP7/dWq49oThEuYSUrrvXj2inhFqkzUC11FTSmmHCSDXfrGVSpu/Q/eR+sWK473wEB6mXXMe6eIHDiO/tGTsgIg7SCL6jf4jr87JaaMM4ImWh3cfDx0Vt6FuMeRC/xaXxXxX6x0AqeCK1Czq1tU43B4Im88zwERJmInP1vJRwHCJTVqS2cxh3Iv1pESY1equm88YJNbZDXOumidy95grcGz060vhkoWI1JyVf1Nu7NeUFNjNkntjmhKSl9d6V/lXcWp4eR267bulyJaypShUUUAG/mTvPMx5zsJpqvAVVGur0XyQAbTNeYfdTqL4+sfEQUf0cXdT9we3pJtfNqRcFWHJkvQRDGSvYRos4vLYJ5a4rIcYA/dvQMf0uKAnkQO2KbaJ5FQwKkVBBFCCNQRuMb2JcZX6WAi2iT+HhZ0cs/v4SoUEcQN/McI0QoxrRVvh2qE56J7qDTpttmCqSFIT/uMMz3JX+sRcLArzppmcTnyEEdjrpFnu+VKK9Zk6SYOLTOsQewUX+WH7tldEr17AAMgOFYVv8AUEXtIrWE2AJ65Cg5ots9uCGTqo16ksgTEANDThESz2YKMsqAkd2sdZLSGxGlTiy5iuXyiQwKq2L13atBmcOigncNTTnC1hJBc89ZU6qiuXdS7AgxUpT70hrajqqrDVWB84nXPZm1IgLthaakSxvPAjsicNpAb4m3AdeqrN30R+75mJAeMNWu5ROtNmmsMrOZkztYqFQeJLfyCOuRKIo5QdTIDnnD60ktBOdj6IC4AOICA3i1Zmu/yAhU1KqCc94HPSpiPaEOI8yQO6gPziRPbQctOzKsIJfjcXuP5JujwFAAEItlp/FlJ+ardm74GDdtILZgcD8WHjECVZV6TpCK07e3uiRNbE/aSfP78Im6LRlBvv5U+ykQCR4BJvNgtnbF7udezSMv9Jd29JYbPaKdaUQjH8j/AEYD+oxou0VpoqpvLA/05/Gg74HbV3bW656MK0klv5kGMeaiGHYNXOiHSgHkf8oZPWa3fVfP9ltBU0OY4QVWWCMSZjhvEBQsSLFPaW1RDfKx8Bwuy9kIjQ63bn11VGZU4EYXzHHhDc6zlCCDUbmHzh9ZazBiTI71jyzTqdVhVTkRwg3QEexWAOpdvMdf4KbaXjzX1xqOIiRYqDPPgynWnLmNRC5t2Oi9Kuag5MOe4w+XM5VKKOkXI0yxLrQ/WKy01qM1wuFLZddeCbqnv/5Y6Pegmfwpn9MdHu06uodn4H0Vfmn2Qan2m4n6ROua6HnzpciWKu5p+lfac8gKmGklCWuI67o1H0Q3HhkvbJg686qy67pSnM/zMPBBxgA7uiqKDvK63TdqWeSkmWOqgoOJO9jzJqe+JMxwIQ5bFlp84TbXEuoyLHU8Bw7ICT8+JZlhU+1a/Pyt8CX7Q3SmtYUVNAeH+0eyLaGYCmZAPjAWbNxVGp+uUTUYVxb6Ur2Gg+EAG7XmcWJ7rbqCnsiBk4dKURpZgJAHCsB9rdm0tknAQMSsHQ8CD1h2MtV7xwiUZwQqePVHka+XnBqS1QDDBsye/VNrqPnch0zL9mfAp2gOmkBNq7RglOBvAGXEmlaxMui0h5dQag6dkRL2unpNGpVgTXPkaeWUVbRl4sZgfCG6o1pfJWysRrH0dkq9crBcK0qzkADgN5i1LYlGbU7TAqw3c0ucrYMgKE11J390JvGdOcGWsshc8zWtBkOysLrYRYSXMOLxB9qX63ok9+M9021NQp15XxLkrrnu4nuioSQ8+Zjbj4CuQgpIuFmbFMJyAyrXzgrZ7Eq6CCcns+LEcHxsvG3ID31OSzxJiHDBDLlS7sl0AEFWzitXzfC2foE9ufPlyUH6nGM9y176cYtCwyAUQmt1X74n4D1RVixH6a/WtYiSJBriY1MHrwsWKpWmKlDXRhwJ3dsCZtoKZPKZe0Ej+oZecJW0tnRobzhBLSbEAkU5Vp1SyNy0w1zABnre/XRulyySYbxhcTsaZCghlrUzeoD/ACisKk3Q8w1mmg4VzPhpFMvKx4xwNaT4kUA66BVsR7WCriB7qJY5DT5vSEdUGvbTQDkMz29kEdoJX/ppw1/CccPYbwgrKkhQABQCAG370sFppq0pkUb2Z+oqgbySwAHOHOTlmy8LAOZ3nrqqCTEYxX18l81SlifYbumTmCSpbzGO5FLHy07YvGxPoynWgiZaqyZIwsFyxzAanDrWXkBUnPreGvSUlyFWXLGFFUIqruVRSmeZ7YnMT0OAATfr/HmosguiGgWTXL6KrwNGdpUjfRmLN/SgI84MXl6N53RNgMp3NDkxWtK6BhQE147o0Kda0RlfrGgpTPhllvPbCLutOFWOCrOThUeyOZ3axmZ/qktdhoKeemlr7rfKm7ZIcMWvksLeTOs7GTaEeWDuYEd4OjDmIhyprSZgIOYNQePCPoK2WVZq9FNliYDXGGAwjfQV1IqIxPbq5RZJ/RAky3GOUTmRnQoTqSDTPgRvrDLI7YhTYoLOGnx0TuzQyPJOguroc/upP/Ev/sy/A/WPYp3StHQS7SDuWfsnb14JbWm0S5Kau6ou/wBZqVPjWPpKz2VZUtJSCiIoRRwCgAfCMN9E1jx3lKJ/6azJneEKjzcHujdnaFqMTVEmDRdZj1uVDXuFfpFdvKcS7E66RYbMOvTipPhWvxEA7VIq5HGnjCTtR5Mwa7z7N+9eaOygAb14pqxkdIiDeczyAqfhBCcBQgQixWPrK1c1xV51FKfPuhwgd0DI30g0WtpFV7NFZue4fLM+EEEtwSS8xsgis3gCREa6pJmMWIpQEGtc6ilRAX0iWsWe7LQF9v8ACU7ziOFj5nwg5sJj2uLt4I9gD5n0Q+epTDup8oP6HtphNlmzTD+ItXSvtIxqQOaknuI4GNOEfKllnvKKTZblHQ1VhkQfvdvrG/7CbUT7VLH7TZZ0p8vxOjYS5nMVFV8xz3Q1UQlWphHFIdwiG5jgREmmqkBuTM3KBdutqSkabMYKiAlmO4D70gftXtfIsa/i4yT6qqpJY8AfVHeYxbavayfbmo3UlA1WUpqK8WPtN5DcImGkqJNFIvna1rTeEq1GolSJiNLXgiOGJI95qVPcN0fSEpgcwajd2bo+UJMug5mN39E+1C2iyrJdvx5C4GBObItAjjjlQHmOYjpaoh1Ve4beFBo8aIqaaMeKIUxjxTHF5c0VPa+z9PMs8mpCLME1qasUP4a8hiOI/oHGLLb7WstC7GgH34xV7pLTZxmtvPgNwiiO+4hjM58NVNjc3HT3VuskvCmW4eEAXm0c7znnyJAFOAg3ajSXTSu/sivzH/ENBQYR5EwubajYX9m21B73y0tTzROQh1aXFPh+MOy54GukQnmUPE6x0lSxqdBnC4CReqIlgpdEUnkgYVIFcyaDLkNc4onplusNZul9qSwcH8kxgjDxwnui+2Za5wK2vsv7TY7VhFfwWRebKC2Xfh8IZ9jPf2gPVADXlkhk4BhK+bv2xo6IsdDb2796Edm3ctE9D8wLeNPekzAO2qt8FMbaix84bN3n+y2uTP3S3Bb9Bqr/AOVmj6UlMCAQaggEEbwcwYhFbeq8w2XjLQq4GanxBFCPvhA2ZKPTN2Vy5nL4wZUQ21lqCBlX7+vjC/tbZz4wxws93KlvQXOg8URlZkM7rurqvyFwVJNK/enjEixUZs6mmfgPrTKJNsuxnqKUpQKeVN8IuyzsRQChoQe3QQs9jExYSDXdQ70TMRuEmqdu13dtT3eUVL0mXXPt1okWCzAUljpZzmuGWDVULHeT16DU4eRI0q7bvEtfiYamBVxYRTEcTHeTxPHcO6G7ZskZaEA/M3PhuHnnwohE1GEV3dyVV2Z2LsthUFV6ScNZswAmv5F0ljsz4kxaMNAXc0AzPGnyhNmWrVOiivfu+fhAq/rzNCi5k1B5cY9OzvZ1Hl4mnVdbHdeUvAxJNovUmYyJkq/dST4R4Xamta6wMmAr0atlhBy/NnmeJifLngiF0x+8cTkT7IADCEq02VZ8lkmKHRqgq2hFBlyPmMow7arZh7HN0YyWJwORv9xuDDzGY3gbqZLBQq8GPeeHdTxgPeNilz5bSWJpMqjKcyGIBEwcwVr3CC2y9pvEQQongL5grBNSrS0uasJltQgwQst4TLJaEtEg0ZTXkwPrKeKkZf7CB9pktLdpbesjMrdqkqfMRMu+U04iUqM7n1VUEk86DhDZQILWhW87J7YyLcgMtsMwDrymIxKeXvLwI8jlFiE2MGsfo4vKocS1lEZhmmopB5FCSDB6dZr9s0uomrPUbkKTWAHIgM3dUxUYbSaBwqrml1LgrVp00QMvnaKz2VC8+aqgbq5nkqjNj2Rht47W29yVe0Ou4qoCUO8GgBEV6czMcTkseLEk+JiZlXDNR7Zui1y6r7m3pNmTKFLNLOCWh1ZzQs703gUAG7EYvdzWLAIrfowuzBYJJ3vimH+diV/y4YvcmXSMLoQEQv1yWjGcOFIt0uqaVpnFTtKnJwNNRxEXSBdvsBLYl7x9IA7YkHxCI8IVIsRvHh8ojIzIh9xyBKmIgjOu+HZaYjhXPia6chDiSCCyjIbt2u6JFkk0FFHCpHn3wtMhl7sPXXsijogAqF5eDYVWTLyZtTwG81ifbFWRZ6e6pr4VNYVYrvo/SzNdFXWnMwE9I16iTYLS9czLKL+qZ1F82r3Q5bLlHQ6xHChNgNzfygc1GD6NF9T4n8L5fjoVHQXosiJukal6MdtlVFsdpcLhoJLtpTdLY7qeyeGW4ViXb6K57gGdNSVX2QDMI7TUAHsJgk/odBGVrNecoU/1xpJabFZgHDJacDD8uM6sViva71wgJbZC6KGKzFHLEK05dblSJVm9J1lzWbLnymGRVkBoeGRr4gRV2Ljdt+H2zVuMDOy0FYekINYze2elexoOok6YeShfNiIB2Lbu1Xla5FkljoJMx/xMJJdpagu4x5YaqpGWeesRwPGi7jC2a1TssoHND05qwgLFNbqyqQ7YUY/ekVO3KzDCu9j3j6b++LXaUqpHKK7aJTAHw7stIVtsYocWulD6mv2RqRILVAmigRRuHbnWpiZYxxiEkylBTSue+hgjZ14b/v77IBxDRb3WCn2aZUdkMXkktAk4g41bDl7VdAYdsyUz3b4HW1xMrNb9xJBevvFRr4CCOzGviRBQfilL8qedlhjForXLq3NZTfl1G1XraJUoqueIk1IBEtMVcP5yRGhbO2SVYpWCSBiIGOZ7Tnmdw4AaQMuW7mVS6qMbkvMaoqWYktUncD5UghKs51ZhXcBnG6f2rFiOLIT8LBa2Z8ai4ruspyezoTBiiCrvbrepz2onOOS0mBbzjWkS7LKYgnUCldd9aQFMEG9PH5+EWwtAXt63RItanpZYLUycUVx2Pv7DURnG0OxU+zgzEHSyR7aDNR+dNVpxFRlujUbGhFQcocs9q6O0Aey+RHPjBzY+2I0CKIEQ1ad+n460Qaf2dDiguYKEXtqp2xJAsVmA/gy/9CxY0MCzYwi1lCgHsjSn5Ru7IXZrZWGV7u8gYFkUrHQ0kysLBjgXl6VEJx00jmaGJrx2l6r1V02bGJ+mzaLpJiWNDknXmU98jqL3Akn9Q4RfdvdrEsMgtUGc9RKTifeI90b+4b4+drTPaY7O7FmYlmJ1JJqTFgC4maR0dHR1dX1tMnYQaCrAVp/eGZd5UNHDA8ApYDicS15RAEwkYjqdB51hxZ4QiubeQ+wYUpjasVz7Gg63XJ8MvAGhRWHKNAyqeuXopdlvTG+Eigz1yOlaU46xF2h2Zs1tFJqdcDKYtA69+8cjUR7OPSVFab6jI13U5xNlzTQEkaacxkYuktrPYe8ajfr0N11CPJtIsKLD9q9kZ1iejjFLY9SYBkeRHsty8KwZ9DlmH7ezU9WRMYdpeWnwYxrtpssufKZJih0cUZT95EHfqKRR9lNmmsF6lalpM6RMEpzxDS3KNwcBD2jPiA3/AKgRYZ3080D7AsiCmXsr8wrDkeUhZjCFrKbiLaLGGzETaQpViqLBhxmYIgqFOHEcw1aqzabuYH1D3UMKs8hwRRDz5eMHBOBNN41HOF0gO3YkrEo9rnUz0+3uthn4je6QEMS7i2Tnq1rhGnYTv7Ire397JKWTY09ae2YG5EGI+JAHeYtV7XklnlNMmMFVQSSdwEfO1u2ma0XklrmGiCYoAPsysVCO3CSTzMFGSrIUIw4QpUc8rX6tVZxGc54e85Hr0Wty7LWWMJpXOvGGpMqgIahO4iDtnu+icvGnMQGnUGhBhPjwIsu/BE1uOHWY08kyy8dsUd0oakshoOSCQtK0Bz7aaQODZ6RMRjiAbh/YRW95pVXvFU8rCh3njA22zqzZfGv0h+fNCluG6GrjsDT52I5CvlHZaC577XJy5qp72saXHJXyzHKBN9yTLPSr6pPW5E6GDSLSEWuUGRlbQihh7ezEEo4qFCLBb6wWSdGQTNu5dmnTJE+VNDS3ZCVwsDhNAwqQaEUOm+JD+l6zqOpJnMeYRR44ifKIwsX+4KTgNCtWaZFP2125kWJStRMnEdWUD5ufYXzO6KvNvq9Lcv4YFklt7oLTKHixpTuAMAZvoynEkm0KSSSS6NWtcySGNTFLtoSsN2FzwFYJWM4VDSqVfN6zbVNadObE7eCjcqjco4RESXF5tfoutyKXTopyj+G3WP8AKwA84rl32T/1KSZyOn4iq6sCrKCRWoIqDQwThhpWR5IQ7oI6Ny//AB5d/wDDf/yN9Y6NP9tV95HbVaDWPJVmZ601ArDRGecO2OeEVjqxyj5XDLXxMUQ21TgQWtowXXS2oaFqU+9eEPyrRnQinAxDSXkTviVZ90ZXAKbwKI3dbGhFKDUd8T+jUlcQ9U4geBzFRwyJHYTES7X/AAh2tTsBp8okFo+gbP8A/Wh8Bn6eWXJLUz+67ilzBQwmKptVtR/h86U00FrNOqrEZmVNWlGA3qykVA9yo1NTl33rJnoHkzFdDoykH/Y8o2FUqeYUsMo2WucezLSijrMI5lc2HiugVsEibZgXx6GmcRL0vOXJRndgqgVJJoAIYt95uRSSoJ/MSo8gT5RS712EtFubFa7YQmolSkoo7WZjiPMjwiuHhyhixuTpU58fbxUnAj6ln+322j25+jl1WQpyByMwj2iOHAd53UqgldUxtEv0P2MDOdaSeTSh/wDXDdo9EEmn4dpnKd2MI48FCxoaA0WVZJVk9G17/tVhlOTV0HRTOONKCp/UuFu+C14XHLmVYdVjvGh7RFK2K2ctl12lsWGbZZwCuyVrLcepMMs5gZkEiuRBOQjSqxTHgsitwPFR15FWwor4TsTDQqpvdRl5kFv0/QxCmFmbJGy3dsXZkBjxZI4QFfsSGX1aT7omzajqd4XVOFyzZjCoy4fWLXc13LKGmcS1FIWrZRulJGFAOJtz4rHMTcSMKHJc0NuMoWDHhghRZFhG32z/AE18OoOFWlpMdtaCmA0/McIpBa4tnLHJIIQs40ZziPduB7BBra0L+1zGGuFFJ7AWA/znxgesjEC1dB8IXtpTTy8w2uIAtbVHdnyrMGNwv7KwC1KgBXj4c+2PDagSSWrXMnjXOAsuazKEqSKnziQgw5GoPOAJh0FK9b0VEIc1KuIzFZixZQzHDnTLUVoe2H742fs9sf8AFULOIASeMmUrmtaZNnxG+PJMw5U1idbD1Q3HT78YnBno0vGD2Ei+VbHllffRZZiVZE7rhnrqhn+GXxxsn/yx0F/8WncY6Gn/AMjl9zvJv3QL+lRN48ylW+WO7LtH9ojNLpBi12Zcq5DTPyzgY8k5Dhv5cIVJuCWPJPXyOdPZGoEUOAXsoU3Vh275ZLFd+dPrC5VnJ0FYJ3dZSlSdTrFmz9nRJl/eBDNT9q799D8KqZmmw2nepdnTCqqNwpC48pHsPLWhooNEAJJNSqF6YZINgLEepNln+omWfJ4xa7ZVo6ULZDN6RsgJRZWPbhIyHE5CNx9LIxXfMQAlpjylQDe3SqR3ZGBewF0y7LQCjTWH4j8d+EcFHDfrFUaPDhfWet5UocNz/pRTZLZe1oge32ya7kfuleir+px1nbvAz36xZTJl78zCbRaOdIgT7Ua4VrzhWndpdo6jRQeGfPqnFFIEqQM1PwJuA8hAy3tOXOW5DD2WGJT8/AiEdIdxhbTqgAn/AHgc2eisuxxB42Woyw1uvbi2iE1uimL0c0bq1Dc1O/s/vFiXOM42hkFaTUyZTUEduf1i5XDeQnSlfeRn2jI+cNuzJ8zLO9mhk5K9mcTcijIWIdtQqMS7t3LlErFCXzgmRWywqLZbQGFYkq0Vxr0lybX+zu2AzFxy66NnRgDxB3cCIOh4i24vmM10p546W0eAw3WhjwFFxP1iPbbQERmY0ABJ7o8tNoVFJYgAZknLKM+nbVC8Js2TZ85MrDif+IxJpT8gw67+zXkR+BpOvVF1jcRAUYlprM51ck+O7u0ghLsJCFgaGlD8xBG6br5RIvW7Rix01Ar2iFuflXNg9tXLPWqOScyMfZqBd9mlhagEmnGGrUKjSOlSmXjThC61gGfqrWqLDOqiWeaQcwYl2mZRMYzoRlpqafOFWedlQiJlhsXSMBh6gYFt1aaCLGNdFihjRcqEaKGtJOQTnSP/AAx5x7Fl6fkI6GD+hS28+v3QD+oO/iPNc1DCOhXXCPCKD6OvSAtrRZFoYLaQKAnITQB6y/n4r3jlfMcH3wxW4Q0PIyKeUCHQIjy2iQsdXqrwiEOYW5it7U7USbJKaY50yAGrNuVRvJiLnBoqV0AnJCturcC0uSNQcbcsio+J8IHXNN/EiubM2t7YHnvm7zGLflpQBewKBFqsNmwt9/e+Frapd3i7fTy/wisqBQAI7MmE0ENLUjqipJ/3Jjx1OQG7WJ9jmyxLYH1iCB97oX4TGxH0cQB9tOdh1REa4W1Aqhr136w2Gh20nKGJWcVgWqtLcqpq9ZdZLdh+EK2Cc9Gw4MPMf2hN+zMMhuYp3nKJexNmKya+8xI7Bl8jB7YIJfXj7flDp+nZFWlIdhtBDohtCArJvTrZh0dlmb1mMteGJcXxliK1sZtZedRKkyzalFKq2RUbqzdF/mrGl+ku6BaZEtC2ECcrE7wArhqcyDTvhzZGwSpKYZUtUX8o1NKVY6sctTEHOaX4dc+C6AaVRG7J9rKDpZCSz7omh6d4URAv2/LXIUtKsMydQey8v/TXEe4GLTLWPZqjfEqeK4F827VbYWy1lpc78JAc5QBWhG58WZ7Mhyi1ehRARal3hpZ7iHA+BjSNpNlrLbBSdLUkaOOqw7HGdOWkUjY/Z+fdd4FJnXs9oUos0CnXU4kDj2WIxjgainCPd3Lr7+a9fNadZpAEP9HWFppDgji8htouiW24js+kQmuUiuE1qKZj6QdMMu+cYI2zZaJcsHK3stTJyM2wchNl2dHtNlvygsUVQFUUA+84VjhotEpeRhQDWGKE63J9SVCLMxIn1mq7FHQmsextwrPVfJ8tiCCCQRmCMiCNCDuMaFs16TrRJAS0L06jLFWjgc9z99O0xnyiHpYggGB1iqC6i3e7vSPYZgzmGWd4mAr56HuMGrJtdZ5tRJmLMI1wdanbTSMV2H2ZNutGA1EpBimMNaVoFB95j5AndG52K6JUpBLlIqIuigfdTzOcUR2NZZpupscXZoZbrxnzKiWAObVp4DM9mUU28vR3aLW5mT7Zib2QJVFXkBj0840+XYxEiXJpGRrKGpN+XQVxdUUosy2Y2Ktdj6QBpUxGIYULK1aUNVIoKgDedIMoziodGV1zFQc+I515RexKoIS8oEUIBHOMk5I/qAaOpXmPvfiroEx2dLKtyutpvHn91hHREbjBefduEhpfep07uBiK16ygCjPhIFCDkR3QqzGy3wSRENNxtQ+yLwpoOHcv8KAh5Vh0VGi92QjyZecrSXVjyG/viBOsk+0dVj0UveFzZuROi91YzQNnR47qNbbfornx2tFXW4oXb1e0Tllj1VzYggjyOvKLtdkkKoUCgAAHYIiXZdCywFVQAPvOC8tKCHGRkhLig66KETcz2tAMgnVji0Ns9Izn0g+kESVaz2Vg041DOM1lcaH2pnLQb+EEVhJVhvyb00wIuaqTX9Wh8KU8YK3ZZ8AAiHsvYAlls41PQy6k6k4Fqe0mCdqm4FJ8O2MryIQdFd0ArmgvIYEi8bwKCi+t8IrU68yTUk15xMvG0ihqddP7+UVmbO6xhSmZiJNvJiGrRkNB8E+PjaiZJKVbDZYX3o5IvAk01gzZbUrrR6Eadm+p+vKKbKmQUsloIpFUvFfKPxwbbxoRwU5iUZFbQq1y52E0JqDoYmmZAKyWgeqc1PHceEdLvVVndA7UemJAcsa6VU76HIjUZcRVvk5pkxDD2cxuOo+yW48F0N1CjhaIqNUmEvaBSGpb0jZRZqqY75Q1jgbel7SpKY5sxUUZ1Y0jJNufSU08NIsdVlkUaYahnG8KNVXmczy3zDVzPJap/wAU2P8A/pk/1r9Y6PmTojwjoswHcuW3qXKiQgiLTCabt0TJUamblmiLbPRJYglhEymc53YnkjGWB2VVj3mLzLip+jWYGu2z03CYD2idM/374tcsxjimrytDPpCkqIVDamGLwtfRri36AcTFL3tY0udkLlWtaXEAZlPWm1onrMBDBvEGlAe05QDWbmXmZtuGWX3wiDMtLVqTCrH27Ge7+zQDzPPQHkeJRmFs1v8AuNT6K2rahvyiFfV0pPWuQYDqt8jxEDrvttcnzEEEn9EczVDoKeqOP9o1Su1hF7kcCmRO7jvHiLhURpMwzVmfvw6/OfnbGzWaa0i0LMlTENGDISOTApWqnUGDdm9IF3Ef8yg7Qw+KwK9MezyzZAtSAdJK1PvStSP5fWH83GMq2auB7XMwr1UX124chxY+XxYGtDBQaIe5xcalbkvpAsGizukPCWkyYfBVMSG2rxr+BImMd3SfhDzqw71gTs/svKkqFlqAN/EniSdTFnk3YBuiNXnIUXCAFnm10y956kJgEo+xIYhyN4ZmoT2LSvAxl7yyDgZSpGRUgqRyIOYj6a/YBAXajYmTbE6wwTQOpNAzHAH3l5HupF7HEWKpe2uSJ7MTcdisr+9IlE9vRqD51iFtO5CCm9vlD2wVlmSrGLPOFJkh3lngVJxoynepVhQ8jvBh7aWTVK00gTtSH/Ze4blvkHARW1VMnz2IziHgMSwM49mLCu0gWTWDSyZlLBu7rGxwFT6xK8aHQgjszgbLWDko9CChQF+NSCrUyAI+zWLIRZXE/IU88wLb6EeuijFcaUbn17VC8KYSy8DTwgV6Qro/a7CXWvSyR0ssjWqirKKZ5geIEHbWtQkyoLOKtTcRQUh+zr1cHEfGCOyT2MzEh6GnrdvoaINtAB8MO16qsBu/b68JIAE8uBumAP8A5iMXnE6d6ULwYEBpak71QV/zEjyirXlZOjmzZYzwO6f0sV+UQyIaAghCm3nes+0NjnzXmH8xqB2DQd0dYZFTU6CI0iUWIAg6ZGECWNdW+kEJOXLzi0+VnjxMPd3qN03KOgt/hDcI6DP6GIh/6qDvHmg0qWHWnH1T7re6eR3QiS5HVOoh0GhLAA++o0IOjjkfIw/bJazAJietv5wEZdbX2scvYrUfQzewaVNsxPWRukUfkeganYwr/OI0uWY+adlr9ayWmXPFSFNHUe0hyZe3eOYEfRtgtiTEV5bBlYBlI3gioMZozb1CuYbUKIAwHvqf1go1Ar4/7QVUwEv2V+IGz0pWAO3HUlCN5A+fhEtngGNU7ihbzO8w3NoAM8yfKPZgGetYQstWIrlSFAWTDVSpKUGIwSs5LLu6udDvBypA612qtANPpEq7a8co84hjqtNdN3DfrQ8lXEBLKlQNsAP2OYK6I4I/IysPnFR2NsgkyUX2vWb9RzPhp3Rod4WQPLdSPWRgfhGf2SaQBDLLzDmSoLuHGlh9kM7EPiUHVbq5Wa9AugqfKJv+NsFxUHn9YqSzqCHv2olaQOiT82TUPpwot7dnwf4q5Xffav6wp2QblUOYjOLFNIi2XNayoXERhfnoQaRtktrxREwR7t/lkRcCppQEXpl6LFObOawYoflv4KxYBQxAtsgOpU6GJoekMzIZC0EEEIMDS4Wc3pZCjkU0iKprF8vOwrMBB8Yrlpudk3eEKE7Ivlja7dDu4/fI5pmlJ5kVtHWPWSRcEkNNVW0PxBB+UT7xDKSCaljiJ8SB4k/dIauuQUdWI0r5gj5xLmpjfjoO4AD5Rl/Us/T9m36i4jkQBf1HMqcR47XEcgPUFN3XZCxqR1YJWmUBQ8IfJCLFR9JG1KWOzMAwM+YCqLvFcsfYPpDTISDZeHhIvmeP4QCbmjGfi8lg9/WkParQ6+q06Yw7C7ERBdhSG4kWWUCQW9Xfz5CCrWkmgWQmmaI3WnRr0hGZ9WvGDt1SKBrRNFQP8zHQQPsMrpTVspa6A7hBF5/TUHqyk0HzPEmGeVhljBTreUHjvq4158NGjijf/Hk/+BZ//H/eOgN08n3Xjol2EvuVf6t/8T1zQULQVGVDQj3CeW9D9826kZgZbx7vMcVO4wRRhNGJeq4yIPwI3qYhzRhqQCKajUpxH5khcDqGhRYiyizpYbrLrvHGLv6MtsxZ2FmtBpKY9Rj/ANNjqp/IT4E8DlRitDiXTWnDs5R5UPrr8YucMYoVBpw8PZfUUqcCI60yw60MYZsjt9NsoWRaMTyQQFOrSwDu95eWo3cI1q6L4S0IJkqYrrTUEa56jcdMjGCPADgWOFQbFaYcQgghNWqwFYi9GQKk+Q+kHZiYtaHTxoc4iWu7mIIU608KbuGcKczsOKwkwrjdqjUHaLSKPsUJlgswAzMHrJZaClcxrEex2Ey1oDnx8a/KJ8psJqdO7l/eOS+w4sRw7Xut9fRcj7QbTup+8JgSQ7HcrHwBMZfY5daRP2s2u6S0yrvktiLM3TEZgUUlUHOoBPZTfHtlsjK1CPhvqI3bWwwwxgsAFzZrqkk5lRHOcSJIh2bZTHSpZgGXAiyYBkpMsQTsLZNU0oAQOJqPlWIEpInyZWVQe2MxOdq2PqKfPQVcWlKFXCxTsUpTvGR7R/akCdoLxeRKaci4xL6zJvZBm4X82GpHEgDfEy6ARJ7Wy7gIiXmuNGT3gV8RSHmQe58tDc7MtHslKYaGxXAZVSrtvWVaZSzpLh5bjIjzBG4jeDHtsFc4+bNndpbRYWDyHyNMSNmj9o48xQxqdy+lOyTQBPxSH0OIFlJ5Mo+IEdnZVs1BMM9HRQhRDDdVXDMwTskkKKnWK3K2ssOotUj/AMifWKftx6SkMt5FkONnGEzRkqg60qOuSKjhnvgRsrYroD+0iCrhluC0x5ovFBkie2vpJSzlkkATJmYUk5D81Bu+MYvel5TbRMabOcu7ak+QA3AcIZYMxqSSTqdYkybKBm3cIZ4cB7rLC57QmJEne2nxghYbIZjcFHkIfslgL9ZskG/6QSkyTNIlyxRN9cu8nhBmWkg27v8APFYI0xmBn7flLRDNKyZS9XefePHkIVaZeKYtns/4hqBVfaffh4qOPKsKYkt+z2cF2bqkgGrH6ROtc+XYZbS5bBp7Ck2YPZB1SWf9Tb9BvrsfFA163nWnvos7GakcN9fuV7/wa/8AHs//AJEjoq3+KnlHRh/qML+Z/wDn8rT2EX+H/b8KVJ/5o/zR7a/3i/pPwEdHRgmf3ncVdB+hvBDbHr4xGPrGOjo83ILg+s8AnbX6oi2+iT/mZn6B8Y6OjsbXgFOF9K2ldBD7R7HRiV7U0+sRrd6rdh+EdHR1q4Vgew//AOzk/wDcb/S8bRafX7o6Ohb/ANQ5N60RXZn1lJtfrN2xEjo6F+L+47iUxQ/pTyRMkR0dGd64/JW2yfuU7PnAu1R0dH0OW/aZ/wAW+wSdH/cdxPuV8stoOyGTHR0XhQXCHI6OjRCyUXKTYfWiUfXMdHQQl8hxWWJ9Z4I1bv3KdsP2P9y33wjo6C8TI8B7IU36B/y+VN2C/fTf+1M/0GKxf/rt+kfCOjoGT37L+XyiEH99vP4QmOjo6F1FV//Z"
      },
      {
        "recipe_id" : 2,
        "recipe_name": 'Boiled Water',
        "recipe_desc": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis amet odio dolorem nulla dolore hic enim blanditiis aperiam repellendus. Cum doloribus expedita ullam assumenda commodi molestias magnam est fugiat modi!",
        "recipe_time": 10,
        "is_liked": true,
        "recipe_ratings": 5,
        "recipe_tags": [{"tag_id" : 4, "tag_name" : "Breakfast"}],
        "recipe_image": "data:image/jpeg;base64,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"
      }
    ];

    const asyncFetchRecipes = async() => {
      let temp_data = [];
      let data = []
      let ing_ids = []
      try {
        const headers = {
          'Content-Type': 'application/json',
          'token' : localStorage.getItem('token') ? localStorage.getItem('token') : -1
        };
        if (selectedIngredients.length > 0) {
          for(let i = 0; i < selectedIngredients.length; i++) {
            ing_ids.push(selectedIngredients[i].i_id)
          }
          const requestBody = {
            "ingredients_id" : ing_ids,
          }
          temp_data = await APICall(requestBody, '/search/recipes', 'POST', headers);
          console.log(temp_data)
      
  
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
          if (selectedTags.length > 0) {
            let result = []
            let tempSelectedTagId = []
            for (let i = 0; i < selectedTags.length; i++) {
              tempSelectedTagId.push(selectedTags[i].tag_id)
            }
            for (let i = 0; i < data.length; i++) {
              let tempAvailableTagId = []
              for (let j = 0; j < data[i].recipe_tags.length; j++) {
                tempAvailableTagId.push(data[i].recipe_tags[j].tag_id)
              }
              let isValidRecipe = tempSelectedTagId.every(tag_id => tempAvailableTagId.includes(tag_id))
              if (isValidRecipe) result.push(data[i])
            }
            setFoundRecipes(result)
          } else {
            setFoundRecipes(data)

          }

        }
      } catch (err) {
        alert(err);
      }
    }


    React.useEffect(() => {
      let tempTags = []
      let tempIngre = []
      if (localStorage.getItem('fm-ingredients')) {
        tempIngre = JSON.parse(localStorage.getItem('fm-ingredients'))
        setSelectedIngredients(tempIngre)
      }
      if (localStorage.getItem('fm-tags')) {
        tempTags = JSON.parse(localStorage.getItem('fm-tags'))
        setSelectedTags(tempTags)
      }
    },[])
    
    React.useEffect(() => {
      if(selectedIngredients.length > 0) {
        localStorage.setItem('fm-ingredients', JSON.stringify(selectedIngredients))
      }
      if(selectedIngredients.length === 0) {
        localStorage.removeItem('fm-ingredients')
      }
      asyncFetchRecipes()
    },[selectedIngredients])

    React.useEffect(() => {
      if(selectedTags.length > 0) {
        localStorage.setItem('fm-tags', JSON.stringify(selectedTags))
      }
      if(selectedTags.length === 0) {
        localStorage.removeItem('fm-tags')
      }
      asyncFetchRecipes()
    },[selectedTags])
    

    const renderRecipesCard = () => {
      let content = []
      for (let i = 0; i < foundRecipes.length; i++) {
        content.push(
          <RecipeCard object={foundRecipes[i]} isEditable={false} isDelete={false} handleAfterLike={asyncFetchRecipes}/>
        )
      }
      return content
    }


    return (
      <>
        <div style={{display: 'flex', flexDirection: 'column', height: '100%',}} > 
          <NavigationBarHome style={{ alignSelf: 'start' }} ></NavigationBarHome>
          <SearchBar
            selectedIngredients={selectedIngredients}
            setSelectedIngredients={setSelectedIngredients}
          />
          <FilterContainer
            selectedTags={selectedTags}
            setSelectedTags={setSelectedTags} 
          />
          {(selectedIngredients.length > 0) && <div style={{
            position: 'relative',
            display: 'flex',
            flexDirection: 'row',
            justifyContent: 'space-evenly',
            flexWrap: 'wrap',
            alignContent: 'flex-start',
            marginTop: '20px',
            marginLeft: '20px',
          }}>
            {renderRecipesCard()}
          </div>}
          { (selectedIngredients.length === 0) && <div style={{
            display: 'flex',
            height: 'auto',
            width: '100%',
            padding: '150px 0',
            justifyContent: 'center',
            fontSize: '3em',
            fontWeight: 'bold',
            fontFamily: 'Righteous',
            color: 'rgba(229, 148, 7, 0.58)' 
          }}>
            Put in Your Ingredients Above
          </div>}
          { (selectedIngredients.length > 0) && (foundRecipes.length === 0) && <div style={{
            display: 'flex',
            height: 'auto',
            width: '100%',
            padding: '150px 0',
            justifyContent: 'center',
            fontSize: '3em',
            fontWeight: 'bold',
            fontFamily: 'Righteous',
            color: 'rgba(229, 148, 7, 0.58)' 
          }}>
            No Recipes Found
          </div>}
        </div>
      </>
    )
  }
  
export default HomeScreen;