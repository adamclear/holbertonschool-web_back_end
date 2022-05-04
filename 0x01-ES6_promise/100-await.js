import { uploadPhoto as photo, createUser as user } from './utils';

export default async function asyncUploadUser() {
  const uploadedUser = {
    photo: null,
    user: null,
  };
  try {
    uploadedUser.photo = await photo();
    uploadedUser.user = await user();
    return uploadedUser;
  } catch (error) {
    return uploadedUser;
  }
}
