import { uploadPhoto as photo, createUser as user } from './utils';

export default async function asyncUploadUser() {
  const completeUser = {
    photo: null,
    user: null,
  };
  try {
    const uploadedPhoto = await photo();
    const uploadedUser = await user();
    completeUser.photo = uploadedPhoto;
    completeUser.user = uploadedUser;
    return completeUser;
  } catch (error) {
    return completeUser;
  }
}
