import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return [
    await signUpUser(firstName, lastName)
      .then((response) => ({ status: 'fulfilled', value: response })),
      /* signUpUser only has a resolve no need for a catch*/
    await uploadPhoto(fileName)
      /* uploadPhoto only has a reject no need for a then*/
      .catch((response) => ({ status: 'rejected', value: response.toString() })),
  ];
}
