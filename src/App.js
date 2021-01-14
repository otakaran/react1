import React from 'react'
import axios from 'axios';
import { Component } from 'react'
import Table from './Table'
import Form from './Form';

class App extends Component {
    state = { characters: [] }
    makeDeleteCall(character){
      // Had to use local ip here otherwise only get was supported
      return axios.delete('http://127.0.0.1:5000/users', {data:character["id"]})
       .then(function (response) {
         console.log(response);
         return (response);
       })
       .catch(function (error) {
         console.log(error);
         return false;
       });
    }

      removeCharacter = index => {
        const { characters } = this.state
        console.log(characters[index])
        this.makeDeleteCall(characters[index]).then(callResult => {
          if (callResult.status === 200) {
            // Remove on frontend
            this.setState({
              characters: characters.filter((character, i) => { 
                return i !== index
            })
          })
        }
        });

        
        
      }



      makePostCall(character){
        // Had to use local ip here otherwise only get was supported
        return axios.post('http://127.0.0.1:5000/users', character)
         .then(function (response) {
           console.log(response);
           return (response);
         })
         .catch(function (error) {
           console.log(error);
           return false;
         });
      }

      handleSubmit = character => {
        this.makePostCall(character).then( callResult => {
           if (callResult.status === 201) {
              this.setState({ characters: [...this.state.characters, callResult.data["new_user"]] });
           }
        });
      }

    componentDidMount() {
        axios.get('http://localhost:5000/users')
         .then(res => {
           const characters = res.data.users_list;
           this.setState({ characters });
         })
         .catch(function (error) {
           //Not handling the error. Just logging into the console.
           console.log(error);
         });
    }

    render() {
        const { characters } = this.state
        return (
            <div className="container">
              <Table characterData={characters} removeCharacter={this.removeCharacter} />
              <Form handleSubmit={this.handleSubmit}/>
            </div>
        )
    }
}

export default App