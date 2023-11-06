export type VideoInfo = {
  id: string;
  url: string;
};
export type RecommendVideo = {
  total: number;
  videos: VideoInfo[];
};

export type VideoInformation = {
  id: string;
  create_time: string;
  favoriting_count: number;
  follower_count: number;
  description: string;
  collect_count: number;
  comment_count: number;
  digg_count: number;
  share_count: number;
  qiniuKey: string;
  uploadedAt: Date;
  categories: string;
  game: null;
  frame_url: string;
  cover_url: string;
  playback_url: string;
}
export type Categories = {
  name: string
}